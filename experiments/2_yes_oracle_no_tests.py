# pip install accelerate
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, QuantoConfig
from utils import get_logger, get_constraints, get_constraint_text, get_second_quote_end_index
import argparse
import subprocess
import json

model_user = "codellama"
model_name = "CodeLlama-7b-Python-hf"
temperatures = [0.5]
num_rounds = 1

def run(logger, args):
    start_index, end_index = args.indicies
    input_folder_path, output_folder_path = args.folderpaths
    t = args.temperature
    logger.info(f"start index: {start_index}, end index: {end_index}")

    logger.info("loading dataset...")
    dataset = load_dataset("evalplus/humanevalplus")

    logger.info("loading tokenizer...")
    model_hf_name = f"{model_user}/{model_name}"
    tokenizer = AutoTokenizer.from_pretrained(model_hf_name)

    logger.info("loading quantized model...")
    quantization_config = QuantoConfig(weights="int8")
    model = AutoModelForCausalLM.from_pretrained(model_hf_name, device_map="auto", quantization_config=quantization_config)

    logger.info(f"computing temperature {t}...")

    for i in range(start_index, end_index):
        example = dataset["test"][i]
        prompt = example["prompt"].lstrip()
        full_solution = prompt + example["canonical_solution"]

        for j in range(10):
            try:
                code_file_path = f"{input_folder_path}/temperature-{t}_problem-{i}_solution-{j}.py"
                code_file = open(code_file_path, "r")
                full_code = code_file.read()
                code_file.close()

                # Trim away everything past the specification, which could include constraints/things not related to code
                second_quote_end_index = get_second_quote_end_index(full_code)
                code = full_code[second_quote_end_index:]
            except: # Do nothing on error
                pass
            else:
                if code != full_solution:
                    code_tokens = tokenizer.tokenize(code)
                    solution_tokens = tokenizer.tokenize(example["canonical_solution"].lstrip())
                    constraints = get_constraints(code_tokens, solution_tokens)

                    constraint_text = None
                    if len(constraints) > 0:
                        constraint_to_use = constraints[0]
                        constraint_text = get_constraint_text(constraint_to_use, code_tokens, solution_tokens, logger)

                        # Find the next available constraint if the current constraint returns nothing
                        index = 1
                        logger.info(constraint_to_use)
                        while constraint_text == "" and index < len(constraints):
                            constraint_to_use = constraints[index]
                            constraint_text = get_constraint_text(constraint_to_use, code_tokens, solution_tokens, logger)
                            index += 1
                        logger.info(constraint_to_use)
                        logger.info(constraint_text)
                        
                        # Identify tokens to keep
                        solution_constraint_start_index = constraint_to_use[3] # Index of the constraint in solution_tokens
                        logger.info(solution_tokens[0:solution_constraint_start_index])
                        temp_code = tokenizer.decode(tokenizer.convert_tokens_to_ids(solution_tokens[0:solution_constraint_start_index]))
                        logger.info(temp_code)
                        
                        assert(len(temp_code) <= len(example["canonical_solution"])) # temp_code should always be a subset of the canonical solution

                        text_to_keep = code[0:len(temp_code)]
                        logger.info(text_to_keep)

                    if constraint_text != None: # Should be None if the constraint is not valid
                        closing_quotes = "\"\"\"" if "\"\"\"" in prompt else "'''"

                        updated_code = prompt[:-4] + "\n" + constraint_text + f"\t{closing_quotes}\n" + text_to_keep

                        input_ids = tokenizer(updated_code, return_tensors="pt").to("cuda")

                        outputs = model.generate(
                            **input_ids,
                            max_new_tokens=500,
                            temperature=0.5,
                            # Do greedy decoding
                            do_sample=True,
                            num_beams=1
                        )

                        decoded_output = tokenizer.decode(outputs[0]).replace("<s>", "").replace("</s>", "").lstrip()
                        
                        f = open(f"{output_folder_path}/temperature-{t}_problem-{i}_solution-{j}.py", "w")
                        f.write(decoded_output)
                        f.close()

                        logger.info(f"{output_folder_path}/temperature-{t}_problem-{i}_solution-{j}.py")

def test(logger, args):
    start_index, end_index = args.indicies
    input_folder_path, output_folder_path = args.folderpaths
    t = args.temperature

    logger.info("loading dataset...")
    dataset = load_dataset("evalplus/humanevalplus")

    data = {}
    logger.info(f"computing temperature {t}...")
    for i in range(start_index, end_index):
        data[f"problem-{i}"] = []

        example = dataset["test"][i]
        for j in range(10):
            try:
                code_file_path = f"{input_folder_path}/temperature-{t}_problem-{i}_solution-{j}.py"
                code_file = open(code_file_path, "r")
                code = code_file.read()
                code_file.close()
            except: # Do nothing on error
                pass
            else:                            
                test_file_path = f"{output_folder_path}/tests/temperature-{t}_problem-{i}_solution-{j}.py"
                test_file = open(test_file_path, "w")

                test = example["test"]
                entry_point = example["entry_point"]

                test_file_content = code + "\n\n" + test + "\n\n" + f"check({entry_point})"
                test_file.write(test_file_content.encode("ascii", "ignore").decode("ascii"))
                test_file.close()

                # Build the command to run the Python script
                # Assumes that 'python' is the command to run your Python interpreter
                # This might need to be changed to 'python3' on some systems
                command = ["python3", test_file_path]

                # Execute the command
                try:
                    process = subprocess.run(command, capture_output=True, text=True, timeout=120)
                except Exception as e:
                    data[f"problem-{i}"].append(str(e))
                else:
                    # Check if the script was executed successfully
                    if process.returncode == 0:
                        data[f"problem-{i}"].append(1)
                    else:
                        data[f"problem-{i}"].append(process.stderr)

    logger.info("writing to file...")
    json.dump(data, open(f"{output_folder_path}/yes_oracle_no_tests.json", "w"))

def main():
    # create parser object
    parser = argparse.ArgumentParser(description = "A text file manager!")
 
    # defining arguments for parser object
    parser.add_argument("action")
    
    parser.add_argument("-f", "--folderpaths", type = str, nargs = 2,
                        metavar = "folder_paths", default = None,
                        help = "Reads input files and write output files to the specified folder paths (input, output)")
    
    parser.add_argument("-i", "--indicies", type = int, nargs = 2,
                        metavar = "indicies", default = None,
                        help = "Only considers dataset values between the specified indicies (start inclusive, end exclusive)")
    
    parser.add_argument("-t", "--temperature", type = float,
                        metavar = "temperature", default = None,
                        help = "Temperature of the outputs")
 
    # parse the arguments from standard input
    args = parser.parse_args()
     
    # calling functions depending on type of argument
    if args.action == "run":
        logger = get_logger("INFO", "starting run for 2_yes_oracle_no_tests.py")
        run(logger, args)
    elif args.action == "test":
        logger = get_logger("INFO", "starting test for 2_yes_oracle_no_tests.py")
        test(logger, args)
 
if __name__ == "__main__":
    # calling the main function
    main()
