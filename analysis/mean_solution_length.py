import argparse
from datasets import load_dataset

# Function to calculate percentage of problems with 1 passing test case
def calculate_mean_solution_length(args):
    input_folder_path = args.filepath
    t = args.temperature

    dataset = load_dataset("evalplus/humanevalplus")

    lens = []
    for i in range(len(dataset["test"])):
        for j in range(10):
            try:
                code_file_path = f"{input_folder_path}/temperature-{t}_problem-{i}_solution-{j}.py"
                code_file = open(code_file_path, "r")
                code = code_file.read()
                code_file.close()

                lens.append(len(code))
            except:
                pass

    avg_len = float(sum(lens)) / len(lens)
    print(avg_len)

def main():
    # create parser object
    parser = argparse.ArgumentParser(description = "A text file manager!")
 
    parser.add_argument("-f", "--filepath", type = str,
                        metavar = "filepath", default = None,
                        help = "File path of the file containing the runtime results")
    
    parser.add_argument("-t", "--temperature", type = float,
                        metavar = "temperature", default = None,
                        help = "Temperature of the outputs")
 
    # parse the arguments from standard input
    args = parser.parse_args()

    calculate_mean_solution_length(args)
 
if __name__ == "__main__":
    # calling the main function
    main()