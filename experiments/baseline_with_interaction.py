import sys
import os
import argparse
import subprocess
import json
from vllm import LLM, SamplingParams
from datasets import load_dataset
from utils import (
    get_logger,
    get_constraints,
    get_constraint_text,
    get_second_quote_end_index,
)
from typing import List

from difflib import SequenceMatcher
from transformers import AutoTokenizer

def get_span_diffs(s1_tokens: List[str], s2_tokens: List[str], get_first_nonequal_span_diff: bool = False):
    s = SequenceMatcher(None, s1_tokens, s2_tokens)
    diffs = []
    for tag, i1, i2, j1, j2 in s.get_opcodes():
        if tag != "equal":
            diffs.append((tag, i1, i2, j1, j2))

            if get_first_nonequal_span_diff:
                return diffs[0]
    return diffs

def get_interaction(generation: str, solution: str, tokenizer, interaction_max_len_tokens: int = 10):
    generation_tok = tokenizer.tokenize(generation)
    solution_tok = tokenizer.tokenize(solution)
    solution_len = len(solution_tok)
    first_span_diff = get_span_diffs(s1_tokens=generation_tok, s2_tokens=solution_tok, get_first_nonequal_span_diff=True)
    tag, i1, i2, j1, j2 = first_span_diff

    interaction_tokens = solution_tok[:min(j1+interaction_max_len_tokens, solution_len)]
    interaction_token_ids = tokenizer.convert_tokens_to_ids(interaction_tokens)
    interaction_str = tokenizer.decode(interaction_token_ids)

    return interaction_str

def parse_arguments():
    # create parser object
    parser = argparse.ArgumentParser(description="baseline 2 (with interaction)")

    parser.add_argument(
        "--data-dir",
        type=str,
        required=True,
    )

    parser.add_argument(
        "--model-name",
        type=str,
        required=True,
    )

    parser.add_argument(
        "--model-download-dir",
        type=str,
        default="/data/user_data/nishant2/code_gen_project/models/",
    )

    parser.add_argument(
        "--start-index",
        type=int,
        default=0,
    )

    parser.add_argument(
        "--end-index",
        type=int,
        default=2**32,
    )

    parser.add_argument(
        "--ngpus",
        type=int,
        help="Number of GPUs to use",
        default=1,
    )

    parser.add_argument(
        "--temperature",
        type=float,
        default=0.0,
    )

    parser.add_argument(
        "--interaction-step",
        type=int,
        required=True,
    )

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()

    # figure out what arguments need to be passed to argparse

    # need to know how to save this current thing
    # need to check whether this current thing already exists; otherwise leave

    # load output dict json file that has generations
    # collect task ids that haven't been solved yet
    # write code to compute diff spans
    # write code to provide interaction
    # write code to process that into prefix
    # vllm inference
    # get generations
    # update new dict keeping track of everything
    # save new dict 

    output_file_name = os.path.join(
        args.data_dir,
        "outputs",
        f"{args.model_name.replace('/', '-')}_temp={args.temperature}_step={args.interaction_step}.dict",
    )

    if os.path.exists(output_file_name):
        print(f"file {output_file_name} already exists")
        sys.exit(0)
    
    individual_results_path = os.path.join(
        args.data_dir,
        "outputs",
        f"{args.model_name.replace('/', '-')}_temp={args.temperature}_stage=generation_step={args.interaction_step}.eval_harness_gens.individual_results.json",
    )

    if not os.path.exists(individual_results_path):
        raise ValueError(f"{individual_results_path} does not exist")
    else:
        with open(individual_results_path, 'r') as f:
            individual_results = json.load(f)

    # Load previous interaction step data
    if args.interaction_step == 1:
        prev_interaction_output_filename = os.path.join(
            args.data_dir,
            "outputs",
            f"{args.model_name.replace('/', '-')}_temp={args.temperature}.dict",
        )
    else:
        prev_interaction_output_filename = os.path.join(
            args.data_dir,
            "outputs",
            f"{args.model_name.replace('/', '-')}_temp={args.temperature}_step={args.interaction_step - 1}.dict",
        )

    with open(prev_interaction_output_filename, 'r') as f:
        prev_interaction_outputs_dict = json.load(f)

    # Load my dataset
    dataset = load_dataset("evalplus/humanevalplus")["test"]

    # Load tokenizer
    tokenizer = AutoTokenizer.from_pretrained(args.model_name)

    # Run forward pass
    model = LLM(
        model=args.model_name,
        tensor_parallel_size=args.ngpus,
        download_dir=args.model_download_dir,
        max_model_len=4096,
    )

    sampling_params = SamplingParams(temperature=args.temperature, max_tokens=500)

    prefixes = []
    output_dict = {}
    for i, data_instance in enumerate(dataset):
        if i < args.start_index:
            continue
        if i > args.end_index:
            break

        output_dict[data_instance["task_id"]] = {
            "prompt": data_instance["prompt"],
            "canonical_solution": data_instance["canonical_solution"],
            "entry_point": data_instance["entry_point"],
            "test": data_instance["test"],
            f"generation_step_{args.interaction_step}": None,
        }
    
    task_ids_not_already_passed = []

    for task_id in prev_interaction_outputs_dict:
        prev_generation = prev_interaction_outputs_dict[task_id][f"generation_step_{args.interaction_step-1}"]
        test_success = individual_results['humanevalplus'][str(task_id.split('/')[-1])][0][1]['passed']
        if not test_success:
            task_ids_not_already_passed.append(task_id)

            curr_solution = prev_interaction_outputs_dict[task_id]["canonical_solution"]

            interaction_str = get_interaction(generation=prev_generation, solution=curr_solution, tokenizer=tokenizer)
            output_dict[task_id][f'interaction_{args.interaction_step}'] = interaction_str

            prefixes.append(
                prev_interaction_outputs_dict[task_id]["prompt"].lstrip() + interaction_str
            )
        else:
            output_dict[task_id][f"generation_step_{args.interaction_step}"] = prev_generation

    # Save generations
    outputs = model.generate(prefixes, sampling_params)

    for i, output in enumerate(outputs):
        task_id = task_ids_not_already_passed[i]
        output_dict[task_id][f"generation_step_{args.interaction_step}"] = output.outputs[0].text

    output_file_name = os.path.join(
        args.data_dir,
        "outputs",
        f"{args.model_name.replace('/', '-')}_temp={args.temperature}_step={args.interaction_step}.dict",
    )

    with open(output_file_name, "w") as f:
        json.dump(output_dict, f)
