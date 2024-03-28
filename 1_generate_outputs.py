# pip install accelerate
from transformers import AutoTokenizer, AutoModelForCausalLM
from datasets import load_dataset

model_user = "codellama"
model_name = "CodeLlama-13b-Python-hf"
temperature = 3.0

print("loading dataset...")
dataset = load_dataset("evalplus/humanevalplus")

print("loading tokenizer...")
model_hf_name = f"{model_user}/{model_name}"
tokenizer = AutoTokenizer.from_pretrained(model_hf_name)

print("loading model...")
model = AutoModelForCausalLM.from_pretrained(model_hf_name, device_map="auto")

for i in range(len(dataset["test"])):
    example = dataset["test"][i]
    prompt = example["prompt"]

    print("tokenizing...")
    input_ids = tokenizer(prompt, return_tensors="pt").to("cuda")

    print("generating outputs...")
    outputs = model.generate(
        **input_ids,
        max_new_tokens=2000,
        early_stopping=True,
        num_beams=10,
        num_return_sequences=10,
        temperature=temperature,
        do_sample=True
    )

    for j in range(len(outputs)):
        decoded_output = tokenizer.decode(outputs[j]).replace("<s>", "").replace("</s>", "").lstrip()
        print(decoded_output)
        
        f = open(f"./data/{model_name}/code/temperature-{temperature}_problem-{i}_solution-{j}.py", "w")
        f.write(decoded_output)
        f.close()
