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

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()

    input_file_name = os.path.join(
        args.data_dir,
        "outputs",
        f"{args.model_name.replace('/', '-')}_temp={args.temperature}.dict",
    )

    with open(input_file_name, 'r') as f:
        input_data = json.load(input_file_name)

    for task_id in input_data:
        curr_dict = input_data[task_id]

    # TODO: things to compute
    # Pass @ 1
    # CodeBERT Prec Rec F1
    # CodeBLEU
    # Execute code and see?

    # Load my dataset
    # dataset = load_dataset("evalplus/humanevalplus")["test"]
    '''
        prefixes.append(data_instance["prompt"].lstrip())
        output_dict[data_instance["task_id"]] = {
            "prompt": data_instance["prompt"],
            "canonical_solution": data_instance["canonical_solution"],
            "entry_point": data_instance["entry_point"],
            "test": data_instance["test"],
            "generation_step_0": None,
        }
    '''

    output_file_name = os.path.join(
        args.data_dir,
        "outputs",
        f"{args.model_name.replace('/', '-')}_temp={args.temperature}.dict",
    )

    with open(output_file_name, "w") as f:
        json.dump(output_dict, f)
