from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    numbers_list = numbers.split()
    numbers_list.sort()
    return " ".join(numbers_list)


if __name__ == "__main__":
    print("Example:")
    print(sort_numbers("three one five"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sort_numbers("three one five") == "one three five"
    assert sort_numbers("first second third") == "first second third"
    assert sort_numbers("seventh eighth ninth one") == "one eighth ninth seventh"
    assert sort_numbers("one ten two") == "one two ten"
    print("Coding complete? Click 'Check' to earn cool rewards!")
