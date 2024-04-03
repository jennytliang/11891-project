import evaluate
from datasets import load_dataset
import argparse
import json

def calculate_code_bleu_score(args):
    metric = evaluate.load("k4black/codebleu")

    preds_file_path = args.filepath
    t = args.temperature
    output_file_path = args.outputpath

    dataset = load_dataset("evalplus/humanevalplus")

    cands = []
    refs = []
    for i in range(len(dataset["test"])):
        example = dataset["test"][i]
        full_solution = example["prompt"].lstrip() + "\n" + example["canonical_solution"].lstrip()
        for j in range(10):
            try:
                pred_file_path = f"{preds_file_path}/temperature-{t}_problem-{i}_solution-{j}.py"
                pred_file = open(pred_file_path, "r")
                pred = pred_file.read()
                pred_file.close()

                cands.append(pred)
                refs.append(full_solution)

            except: # Do nothing on error
                pass

    assert(len(cands) == len(refs))

    results = metric.compute(references=refs, predictions=cands, lang=["python"])

    with open(output_file_path, "w") as file:
        json.dump(results, file)

def main():
    # create parser object
    parser = argparse.ArgumentParser(description = "A text file manager!")
    
    parser.add_argument("-f", "--filepath", type = str,
                        metavar = "filepath", default = None,
                        help = "Folder path of the predictions to compute BERT score")
    
    parser.add_argument("-t", "--temperature", type = float,
                        metavar = "temperature", default = None,
                        help = "Temperature of the outputs")
    
    parser.add_argument("-o", "--outputpath", type = str,
                        metavar = "outputpath", default = None,
                        help = "File path of the output file")
 
    # parse the arguments from standard input
    args = parser.parse_args()

    calculate_code_bleu_score(args)
 
if __name__ == "__main__":
    main()