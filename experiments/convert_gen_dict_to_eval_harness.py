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


def process_generation(
    prompt: str, generation: str, return_gen_only: bool = False
) -> str:
    stop_tokens = [
        "\nclass",
        "\ndef",
        "\n#",
        "\n@",
        "\nprint",
        "\nif",
        "\n```",
        "<file_sep>",
    ]

    end_token = len(generation)
    for stop_token in stop_tokens:
        index_of_stop = generation.find(stop_token)
        if index_of_stop < end_token and index_of_stop != -1:
            end_token = index_of_stop

    if return_gen_only:
        return generation[:end_token]

    return prompt + generation[:end_token]


if __name__ == "__main__":
    args = parse_arguments()

    input_filename = os.path.join(
        args.data_dir,
        "outputs",
        f"{args.model_name.replace('/', '-')}_temp={args.temperature}.dict",
    )

    with open(input_filename, "r") as f:
        data_dict = json.load(f)

    gens_list = []

    for i in range(len(data_dict.keys())):
        curr_prompt = data_dict[f"HumanEval/{i}"]["prompt"]
        curr_gen = data_dict[f"HumanEval/{i}"][args.key_in_dict]

        gens_list.append(process_generation(curr_prompt, curr_gen))

    output_filename = os.path.join(
        args.data_dir,
        "outputs",
        f"{args.model_name.replace('/', '-')}_temp={args.temperature}_stage={args.key_in_dict}.eval_harness_gens",
    )

    with open(output_filename, "w") as f:
        json.dump(gens_list, f)
