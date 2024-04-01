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
        print(f"Temperature {temperature}: {percentage:.2f}% of problems at least 1 passing test case.")