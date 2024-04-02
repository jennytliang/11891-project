from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    
	Include these tokens in the code: if not strings : return None
	"""
    if not strings:
        return None

    max_length = 0
    longest_string = ""

    for string in strings:
        if len(string) > max_length:
            max_length = len(string)
            longest_string = string

    return longest_string


def sum_numbers(numbers: List[float]) -> float:
    """ Out of list of numbers, return the sum. Return 0 in case the input list is empty.
    >>> sum_numbers([])
    0
    >>> sum_numbers([1, 2, 3])
    6
    >>> sum_numbers([0.1, 2, 3])
    5.1
    """
    return sum(numbers)


def sum_even_numbers(numbers: List[float]) -> float:
    """ Given a list of numbers, return the sum of even ones. Return 0 in case the input list is empty.
    >>> sum_even_numbers([])
    0
    >>> sum_even_numbers([1, 2, 3])
    2
    >>> sum_even_numbers([0.1, 2, 3])
    2
    """
    return sum([number for number in numbers if number % 2 == 0])


def sum_multiple_of_3(numbers: List[float]) -> float:
    """ Given a list of numbers, return the sum of multiples of 3. Return 0 in case the input list is empty.
    >>> sum_multiple_of_3([])
    0
    >>> sum_multiple_of_3([1, 2, 3])
    0
    >>> sum_multiple_of_3([3, 6, 9])
    12
    """
    return sum([number for number in numbers if number % 3 == 0])


def multiply_numbers(numbers: List[float]) -> float:
    """ Out of list of numbers, return the multiplication. Return 1 in case the input list is empty.
    >>> multiply_numbers([])
    1
    >>> multiply_numbers([1, 2, 3])
    6
    >>>