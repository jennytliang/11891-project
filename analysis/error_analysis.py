import argparse
import json
import re

def calculate_error_stats(args):
    input_file_path = args.filepath
    output_file_path = args.outputpath
    
    error_data = json.load(open(input_file_path, "r"))

    errors = dict()
    for _, problems in error_data.items():
        for _, test_cases in problems.items():
            for test in test_cases:
                if test != 1:
                    # Regex pattern to match typical Python error types (e.g., ValueError, IndexError)
                    # It looks for words that start with a capital letter and may continue with any combination
                    # of letters, numbers, or underscores, typically followed by a colon or space.
                    pattern = r'\b[A-Z][a-zA-Z0-9_]*Error\b'
                    
                    # Find all non-overlapping matches of the regex pattern in the error message
                    matches = re.findall(pattern, test)
                    
                    # Remove duplicates by converting the list to a set, then back to a list
                    unique_matches = list(set(matches))

                    for um in unique_matches:
                        if um not in errors:
                            errors[um] = 0
                    
                        errors[um] += 1

    json.dump(errors, open(output_file_path, "w"), indent=4)

def main():
    # python3 error_analysis.py -f /home/jtliang/interactive-constrained-decoding/11891-project/experiments/out/CodeLlama-7b-Python-hf/no_oracle_no_tests/no_oracle_no_tests_0.5.json -t 0.5 -o /home/jtliang/interactive-constrained-decoding/11891-project/analysis/out/CodeLlama-7b-Python-hf/error_analysis/temperature-0.5_round-0.json
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

    calculate_error_stats(args)
 
if __name__ == "__main__":
    main()