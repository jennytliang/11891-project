from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    # split the string into a list of strings
    num_list = numbers.split()
    # sort the list
    num_list.sort()
    # join the list back together with spaces
    return " ".join(num_list)


if __name__ == "__main__":
    print(sort_numbers("five three one"))
