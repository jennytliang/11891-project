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


def parse_arguments():
    # create parser object
    parser = argparse.ArgumentParser(description="baseline 1")

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

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()

    # Load my dataset
    dataset = load_dataset("evalplus/humanevalplus")["test"]

    # Run forward pass
    model = LLM(
        model=args.model_name,
        tensor_parallel_size=args.ngpus,
    )

    sampling_params = SamplingParams(temperature=args.temperature, max_tokens=500)

    prefixes = []
    output_dict = {}
    for i, data_instance in enumerate(dataset):
        if i < args.start_index:
            continue
        if i > args.end_index:
            break

        prefixes.append(data_instance["prompt"].lstrip())
        output_dict[data_instance["task_id"]] = {
            "prompt": data_instance["prompt"],
            "canonical_solution": data_instance["canonical_solution"],
            "entry_point": data_instance["entry_point"],
            "test": data_instance["test"],
            "generation_step_0": None,
        }

    # Save generations
    outputs = model.generate(prefixes, sampling_params)

    for i, output in enumerate(outputs):
        output_dict[f"HumanEval/{i}"]["generation_step_0"] = output.outputs[0].text

    output_file_name = os.path.join(
        args.data_dir,
        "outputs",
        f"{args.model_name.replace('/', '-')}_temp={args.temperature}.dict",
    )

    with open(output_file_name, "w") as f:
        json.dump(output_dict, f)
