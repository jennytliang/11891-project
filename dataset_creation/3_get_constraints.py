import json
from difflib import SequenceMatcher
from datasets import load_dataset
from transformers import AutoTokenizer

model_user = "codellama"
model_name = "CodeLlama-7b-Python-hf"
temperatures = [0.5, 1.0, 2.0, 3.0, 4.0]

print("loading dataset...")
dataset = load_dataset("evalplus/humanevalplus")

print("loading tokenizer...")
model_hf_name = f"{model_user}/{model_name}"
tokenizer = AutoTokenizer.from_pretrained(model_hf_name)

def get_diffs(s1, s2):
    s = SequenceMatcher(None, s1, s2)
    diffs = []
    for tag, i1, i2, j1, j2 in s.get_opcodes():
        if tag != "equal":
            diffs.append((tag, i1, i2, j1, j2))

    return diffs

for t in temperatures:
    for i in range(len(dataset["test"])):
        example = dataset["test"][i]
        full_solution = example["prompt"] + example["canonical_solution"]

        for j in range(10):
            try:
                code_file_path = f"./data/{model_name}/code/temperature-{t}_problem-{i}_solution-{j}.py"
                code_file = open(code_file_path, "r")
                code = code_file.read()
                code_file.close()
            except: # Do nothing on error
                pass
            else:
                code_tokens = tokenizer.tokenize(code)
                full_solution_tokens = tokenizer.tokenize(full_solution)
                diffs = get_diffs(code_tokens, full_solution_tokens)

                constraints = []
                
                for tag, i1, i2, j1, j2 in diffs:
                    obj = {
                        "tag": tag,
                        "generated_code": {
                            "tokens": code_tokens,
                            "start": i1,
                            "end": i2
                        },
                        "reference_code": {
                            "tokens": full_solution_tokens,
                            "start": j1,
                            "end": j2
                        }
                    }

                    constraints.append(obj)

                f = open(f"./data/{model_name}/constraints/temperature-{t}_problem-{i}_solution-{j}.json", "w")
                json.dump(constraints, f, indent=4)