from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code:   to _ int = {' zero
	"""

    # 1) Convert the string to a list of numbers
    numbers_list: List[str] = numbers.split()

    # 2) sort the list of numbers
    numbers_list.sort()

    # 3) join the list of numbers into a string
    return " ".join(numbers_list)


if __name__ == "__main__":
    print(sort_numbers("three one five"))
