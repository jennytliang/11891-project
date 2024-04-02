from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    if numbers is None:
        raise TypeError('Input cannot be None')

    ints_dict = {' zero ': '0', 'one ': '1', 'two ': '2', 'three ': '3', 'four ': '4', 'five ': '5', 'six ':
                 '6', 'seven ': '7', 'eight ': '8', 'nine ': '9'}
    numbers_list = numbers.split(' ')
    return " ".join(sorted([ints_dict[int] for int in numbers_list]))
