from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code:   to _ int = {' zero
	"""

    # Convert the string to a list of numbers
    numbers_list = numbers.split()

    # Convert the numbers to integers
    numbers_int = []
    for num in numbers_list:
        numbers_int.append(int(num))

    # Sort the numbers
    numbers_int.sort()

    # Convert the numbers to strings
    numbers_str = []
    for num in numbers_int:
        numbers_str.append(str(num))

    # Convert the list of numbers back to a string
    numbers = " ".join(numbers_str)

    return numbers


if __name__ == "__main__":
    # Test your code with this first
    # Change the expected output to test your code
    expected_output = "three one five"
    output = sort_numbers("three one five")
    print(expected_output == output)

    # Uncomment these to test code after re-writing each function
    # sort_numbers_test1()
    # sort_numbers_test2()
    # sort_numbers_test3()
