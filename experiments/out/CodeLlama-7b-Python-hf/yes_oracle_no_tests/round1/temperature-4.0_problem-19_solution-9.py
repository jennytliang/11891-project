from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    return ' '.join(sorted(numbers.split(), key=lambda x: int(x)))


def get_prices(prices: str) -> str:
    """ Input is a space-delimited string of prices.
    Return a string with the prices sorted from highest to lowest.
    >>> get_prices('10 100 200 1000')
    '1000 100 10'
    """
    return ' '.join(sorted(prices.split(), key=lambda x: float(x), reverse=True))


def get_largest_number(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Return the largest number possible from the set of numberals.
    >>> get_largest_number('three one five')
    'five'
    """
    return ''.join(sorted(numbers.split(), key=lambda x: int(x), reverse=True))[0]


def get_smallest_number(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Return the smallest number possible from the set of numberals.
    >>> get_smallest_number('three one five')
    'one'
    """
    return ''.join(sorted(numbers.split(), key=lambda x: int(x)))[0]


def is_number(text: str) -> bool:
    """ Input is a string of numberals from 'zero' to 'nine'.
    Return True if the string is a number. Otherwise return False.
    >>> is_number('zero')
    True
    >>> is_number('ten')
    False
    """
    return text in ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


def get_word_frequency(text: str) -> str:
    """ Input is a string of words.
    Return the string with each word and the number of