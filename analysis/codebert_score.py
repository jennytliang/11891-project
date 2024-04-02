from datasets import load_dataset
from code_bert_score import score
import argparse

def calculate_bert_score(args):
    preds_file_path = args.filepath
    t = args.temperature

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
    print(len(cands))

    P, R, F1, F3 = score(cands, refs, lang='python')

    print("precision", P.mean())
    print("recall", R.mean())
    print("f1", F1.mean())
    print("f3", F3.mean())

def main():
    # create parser object
    parser = argparse.ArgumentParser(description = "A text file manager!")
    
    parser.add_argument("-f", "--filepath", type = str,
                        metavar = "predictions", default = None,
                        help = "Folder path of the predictions to compute BERT score")
    
    parser.add_argument("-t", "--temperature", type = float,
                        metavar = "predictions", default = None,
                        help = "Temperature of the outputs")
 
    # parse the arguments from standard input
    args = parser.parse_args()

    calculate_bert_score(args)
 
if __name__ == "__main__":
    main()