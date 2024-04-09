from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    # convert input string to a list of numbers
    number_list = numbers.split(" ")
    print(number_list)
    # sort the list
    number_list.sort()
    print(number_list)
    # convert the list to a string
    sorted_numbers = " ".join(number_list)
    print(sorted_numbers)
    return sorted_numbers


if __name__ == "__main__":
    print(sort_numbers("three one five"))
