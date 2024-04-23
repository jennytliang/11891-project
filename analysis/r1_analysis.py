import json
import re

# Load JSON data from file
with open(
    "../experiments/out/CodeLlama-7b-Python-hf/no_oracle_no_tests.json", "r"
) as file:
    data = json.load(file)


# Function to calculate percentage of problems with 1 passing test case
def calculate_pass_at_10(data):
    for temperature, problems in data.items():
        total_problems = len(problems)
        one_pass_count = 0

        for _, test_cases in problems.items():
            if test_cases.count(1) >= 1:
                one_pass_count += 1

        # Calculate percentage
        percentage = (one_pass_count / total_problems) * 100
        print(
            f"Temperature {temperature}: {percentage:.2f}% of problems at least 1 passing test case."
        )


def calculate_percentage_pass(data):
    for temperature, problems in data.items():
        total_test_cases = 0
        passed_test_cases = 0

        for _, test_cases in problems.items():
            # Sum total and passed test cases
            total_test_cases += len(test_cases)
            passed_test_cases += test_cases.count(1)

        # Calculate percentage
        if total_test_cases > 0:  # Ensure division is valid
            percentage = (passed_test_cases / total_test_cases) * 100
            print(f"Temperature {temperature}: {percentage:.2f}% of test cases passed.")
        else:
            print(f"Temperature {temperature}: No test cases available.")


def calculate_program_length_stats():
    temperatures = [0.5, 1.0, 2.0, 3.0, 4.0]
    model_name = "CodeLlama-7b-Python-hf"

    for t in temperatures:
        total_length = 0
        min_length = float("inf")
        max_length = 0
        unique_tokens = set()

        for i in range(10):
            for j in range(10):
                code_file = open(
                    f"./data/{model_name}/code/temperature-{t}_problem-{i}_solution-{j}.py",
                    "r",
                )
                code = code_file.read()
                code_file.close()

                total_length += len(code)
                min_length = min(len(code), min_length)
                max_length = max(len(code), max_length)

                tokens = code.split(" ")
                for token in tokens:
                    unique_tokens.add(token)

        print(t, total_length / 100)
        print("min", min_length)
        print("max", max_length)
        print("unique tokens", len(unique_tokens))


def calculate_error_stats(error_data):
    errors = dict()
    for _, problems in error_data.items():
        for _, test_cases in problems.items():
            for test in test_cases:
                if test != 1:
                    # Regex pattern to match typical Python error types (e.g., ValueError, IndexError)
                    # It looks for words that start with a capital letter and may continue with any combination
                    # of letters, numbers, or underscores, typically followed by a colon or space.
                    pattern = r"\b[A-Z][a-zA-Z0-9_]*Error\b"

                    # Find all non-overlapping matches of the regex pattern in the error message
                    matches = re.findall(pattern, test)

                    # Remove duplicates by converting the list to a set, then back to a list
                    unique_matches = list(set(matches))

                    for um in unique_matches:
                        if um not in errors:
                            errors[um] = 0

                        errors[um] += 1
    print(errors)


calculate_pass_at_10(data)
calculate_percentage_pass(data)
calculate_error_stats(data)
