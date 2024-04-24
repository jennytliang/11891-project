import os
import argparse
import json


def parse_arguments():
    # create parser object
    parser = argparse.ArgumentParser(description="output files to eval harness")

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

    input_filename = os.path.join(
        args.data_dir,
        "outputs",
        f"{args.model_name.replace('/', '-')}_temp={args.temperature}.dict",
    )

    with open(input_filename, "r") as f:
        data_dict = json.load(f)

    gens_list = [
        [data_dict[f"HumanEval/{i}"][args.key_in_dict]]
        for i in range(len(data_dict.keys()))
    ]

    output_filename = os.path.join(
        args.data_dir,
        "outputs",
        f"{args.model_name.replace('/', '-')}_temp={args.temperature}_stage={args.key_in_dict}.eval_harness_gens",
    )

    with open(output_filename, "w") as f:
        json.dump(gens_list, f)
