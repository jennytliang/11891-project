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

    parser.add_argument(
        "--interaction-step",
        type=int,
        default=0,
    )
    
    parser.add_argument(
        "--phase",
        type=str,
        default='baseline',
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

    if args.phase == 'baseline':
        phase = ''
    elif args.phase == 'exp':
        phase = '_constraints'
    elif args.phase == 'exp_finalreport':
        phase = '_constraints_1.05_0.95'
    else:
        raise NotImplementedError('')

    if args.interaction_step == 0:
        input_filename = os.path.join(
            args.data_dir,
            "outputs",
            f"{args.model_name.replace('/', '-')}_temp={args.temperature}.dict",
        )
    else:
        input_filename = os.path.join(
            args.data_dir,
            "outputs",
            f"{args.model_name.replace('/', '-')}_temp={args.temperature}_step={args.interaction_step}{phase}.dict",
        )

    with open(input_filename, "r") as f:
        data_dict = json.load(f)

    gens_list = []

    for i in range(len(data_dict.keys())):
        task_id = f"HumanEval/{i}"
        curr_prompt = data_dict[task_id]["prompt"]
        curr_gen = data_dict[task_id][args.key_in_dict]

        if f'interaction_{args.interaction_step}' in data_dict[task_id]:
            curr_gen = data_dict[task_id][f'interaction_{args.interaction_step}'] + curr_gen

        gens_list.append([process_generation(curr_prompt, curr_gen)])

    output_filename = os.path.join(
        args.data_dir,
        "outputs",
        f"{args.model_name.replace('/', '-')}_temp={args.temperature}_stage={args.key_in_dict}{phase}.eval_harness_gens",
    )

    with open(output_filename, "w") as f:
        json.dump(gens_list, f)
