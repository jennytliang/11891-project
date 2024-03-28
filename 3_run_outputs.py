# pip install accelerate
from datasets import load_dataset
import subprocess
import json

model_user = "codellama"
model_name = "CodeLlama-7b-Python-hf"
temperatures = [0.5, 1.0, 2.0, 3.0, 4.0]

print("loading dataset...")
dataset = load_dataset("evalplus/humanevalplus")

data = {}
for t in temperatures:
    print(f"computing temperature {t}...")
    data[str(t)] = dict()

    for i in range(len(dataset["test"])):
        data[str(t)][f"problem-{i}"] = []

        example = dataset["test"][i]
        test = example["test"]
        entry_point = example["entry_point"]

        for j in range(10):
            try:
                code_file_path = f"./data/{model_name}/code/temperature-{t}_problem-{i}_solution-{j}.py"
                code_file = open(code_file_path, "r")
                code = code_file.read()
                code_file.close()
            except: # Do nothing on error
                pass
            else:
                test_file_path = f"./data/{model_name}/tests/temperature-{t}_problem-{i}_solution-{j}.py"
                test_file = open(test_file_path, "w")
                test_file.write(code + "\n\n" + test + "\n\n" + f"check({entry_point})")
                test_file.close()

                # Build the command to run the Python script
                # Assumes that 'python' is the command to run your Python interpreter
                # This might need to be changed to 'python3' on some systems
                command = ["python3", test_file_path]

                # Execute the command
                process = subprocess.run(command, capture_output=True, text=True)

                # Check if the script was executed successfully
                if process.returncode == 0:
                    data[str(t)][f"problem-{i}"].append(1)
                else:
                    data[str(t)][f"problem-{i}"].append(process.stderr)

print("writing to file...")
json.dump(data, open(f"./data/{model_name}/test.json", "w"))