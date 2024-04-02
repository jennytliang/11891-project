from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    # split the string into a list of words
    words = numbers.split()
    # sort the list of words alphabetically
    words.sort()
    # join the list of words into a string
    return " ".join(words)


def sort_numbers_2(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    # split the string into a list of words
    words = numbers.split()
    # sort the list of words alphabetically
    words.sort()
    # join the list of words into a string
    return " ".join(words)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
