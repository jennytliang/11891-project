# pip install accelerate
from datasets import load_dataset
from utils import get_logger
import argparse
import subprocess
import json


def test(logger, args):
    t = args.temperature
    logger.info(t)
    input_folder_path, output_folder_path = args.folderpaths

    logger.info("loading dataset...")
    dataset = load_dataset("evalplus/humanevalplus")

    data = {}
    for i in range(len(dataset["test"])):
        data[f"problem-{i}"] = []

        example = dataset["test"][i]
        test = example["test"]
        entry_point = example["entry_point"]

        for j in range(10):
            try:
                code_file_path = (
                    f"{input_folder_path}/temperature-{t}_problem-{i}_solution-{j}.py"
                )
                code_file = open(code_file_path, "r")
                code = code_file.read()
                code_file.close()
            except:  # Do nothing on error
                pass
            else:
                test_file_path = (
                    f"{output_folder_path}/temperature-{t}_problem-{i}_solution-{j}.py"
                )
                test_file = open(test_file_path, "w")
                test_file.write(code + "\n\n" + test + "\n\n" + f"check({entry_point})")
                test_file.close()

                logger.info(test_file_path)

                # Build the command to run the Python script
                # Assumes that 'python' is the command to run your Python interpreter
                # This might need to be changed to 'python3' on some systems
                command = ["python3", test_file_path]

                # Execute the command
                try:
                    process = subprocess.run(
                        command, capture_output=True, text=True, timeout=120
                    )
                except Exception as e:
                    data[f"problem-{i}"].append(str(e))
                else:
                    # Check if the script was executed successfully
                    if process.returncode == 0:
                        data[f"problem-{i}"].append(1)
                    else:
                        data[f"problem-{i}"].append(process.stderr)

    logger.info("writing to file...")
    json.dump(data, open(f"{output_folder_path}/no_oracle_no_tests_{t}.json", "w"))


def main():
    # create parser object
    parser = argparse.ArgumentParser(description="A text file manager!")

    # defining arguments for parser object
    parser.add_argument("action")

    parser.add_argument(
        "-f",
        "--folderpaths",
        type=str,
        nargs=2,
        metavar="folder_paths",
        default=None,
        help="Reads input files and write output files to the specified folder paths (input, output)",
    )

    parser.add_argument(
        "-t",
        "--temperature",
        type=float,
        metavar="temperature",
        default=None,
        help="Temperature of the outputs",
    )

    # parse the arguments from standard input
    args = parser.parse_args()

    # calling functions depending on type of argument
    if args.action == "test":
        logger = get_logger("INFO", "starting test for 1_no_oracle_no_tests.py")
        test(logger, args)


if __name__ == "__main__":
    # calling the main function
    main()
