import os
import argparse
import json
from vllm import LLM, SamplingParams
from datasets import load_dataset
from utils import (
    get_logger,
    get_constraints,
    get_constraint_text,
    get_second_quote_end_index,
)
from code_bert_score import score
import evaluate
from convert_gen_dict_to_eval_harness import process_generation


def parse_arguments():
    # create parser object
    parser = argparse.ArgumentParser(description="evaluate gens")

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
        "--temperature",
        type=float,
        default=0.0,
    )

    parser.add_argument(
        "--key-in-dict",
        type=str,
        required=True,
    )

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()

    input_file_name = os.path.join(
        args.data_dir,
        "outputs",
        f"{args.model_name.replace('/', '-')}_temp={args.temperature}.dict",
    )

    with open(input_file_name, "r") as f:
        input_data = json.load(f)

    gens_list = []
    references_list = []

    for i in range(len(input_data)):
        curr_prompt = input_data[f"HumanEval/{i}"]["prompt"]
        curr_gen = input_data[f"HumanEval/{i}"][args.key_in_dict]

        gens_list.append(
            process_generation(curr_prompt, curr_gen, return_gen_only=True)
        )
        references_list.append(input_data[f"HumanEval/{i}"]["canonical_solution"])

    output_results_dict = {}
    precision, recall, f1_score, f3_score = score(
        gens_list, references_list, lang="python"
    )

    output_results_dict["codeBERT"] = {
        "precision": precision.mean().item(),
        "recall": recall.mean().item(),
        "f1": f1_score.mean().item(),
        "f3": f3_score.mean().item(),
    }

    # CodeBLEU
    codeBLEU_metric = evaluate.load("k4black/codebleu")
    codeBLEU_results = codeBLEU_metric.compute(
        references=references_list, predictions=gens_list, lang=["python"]
    )
    output_results_dict["codeBLEU"] = codeBLEU_results

    output_file_name = os.path.join(
        args.data_dir,
        "outputs",
        f"{args.model_name.replace('/', '-')}_temp={args.temperature}_stage={args.key_in_dict}.metrics.dict",
    )

    with open(output_file_name, "w") as f:
        json.dump(output_results_dict, f)
