# pip install accelerate
from datasets import load_dataset

model_user = "codellama"
model_name = "CodeLlama-7b-Python-hf"
temperature = 0.5
num_outputs = 10

print("loading dataset...")
dataset = load_dataset("evalplus/humanevalplus")

for i in range(len(dataset["test"])):
    example = dataset["test"][i]
    solutions = set()

    for j in range(num_outputs):
        f = open(
            f"./data/{model_name}/duplicated_code/temperature-{temperature}_problem-{i}_solution-{j}.py",
            "r",
        )
        code = f.read()

        if code not in solutions:
            solutions.add(code)

            f = open(
                f"./data/{model_name}/code/temperature-{temperature}_problem-{i}_solution-{j}.py",
                "w",
            )
            f.write(code)
            f.close()
