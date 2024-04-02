from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    number_list = numbers.split()
    sorted_list = sorted(number_list)
    result = ' '.join(sorted_list)
    return result


if __name__ == "__main__":
    # Test your code with this first
    # Change the expected output to test your code
    correct_output = "five eight nine one three"
    output = sort_numbers("one three five eight nine")

    print()
    print(f"Expected Output: {correct_output}")
    print(f"Actual Output: {output}")

    # Change the numbers to test your code
    correct_output = "three five eight nine"
    output = sort_numbers("three five eight nine")

    print()
    print(f"Expected Output: {correct_output}")
    print(f"Actual Output: {output}")
