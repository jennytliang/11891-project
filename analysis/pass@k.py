import argparse
import json

# Function to calculate percentage of problems with 1 passing test case
def calculate_pass_at_k(args, data):
    k = args.number
    
    total_problems = len(data)
    k_pass_count = 0
    for _, test_cases in data.items():
        first_k_test_cases = test_cases[0:k]
        if first_k_test_cases.count(1) >= 1:
            k_pass_count += 1
    
    # Calculate percentage
    percentage = (k_pass_count / total_problems) * 100
    print(f"{percentage:.2f}% of problems at least {k} passing test case(s).")

def get_data(args):
    file_path = args.filepath
    return json.load(open(file_path, "r"))

def main():
    # create parser object
    parser = argparse.ArgumentParser(description = "A text file manager!")
 
    # defining arguments for parser object    
    parser.add_argument("-n", "--number", type = int,
                        metavar = "number", default = None,
                        help = "The number to pass to compute pass@k")
    
    parser.add_argument("-f", "--filepath", type = str,
                        metavar = "filepath", default = None,
                        help = "File path of the file containing the runtime results")
 
    # parse the arguments from standard input
    args = parser.parse_args()

    data = get_data(args)
    calculate_pass_at_k(args, data)
 
if __name__ == "__main__":
    # calling the main function
    main()