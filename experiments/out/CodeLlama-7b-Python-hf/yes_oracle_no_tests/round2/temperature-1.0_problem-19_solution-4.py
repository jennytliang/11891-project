from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    return " ".join(sorted(numbers.split(" ")))


def to_binary(num: int) -> str:
    """ Given a positive number, return a string of its binary representation.
    Assume num is a positive number.
    >>> to_binary(10)
    '1010'
    
    """
    return bin(num)[2:]


def to_octal(num: int) -> str:
    """ Given a positive number, return a string of its octal representation.
    Assume num is a positive number.
    >>> to_octal(10)
    '12'
    
    """
    return oct(num)[2:]


def to_hex(num: int) -> str:
    """ Given a positive number, return a string of its hexadecimal representation.
    Assume num is a positive number.
    >>> to_hex(15)
    'f'
    
    """
    return hex(num)[2:]


def is_prime(num: int) -> bool:
    """ Return True if num is a prime number. Otherwise, return False.
    Assume num is a positive integer.
    >>> is_prime(10)
    False
    
    """
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def number_length(num: int) -> int:
    """ Return the length of the number num
    Assume num is a positive integer.
    >>> number_length(10)
    2
    
    """
    return len(str(num))


def is_pandigital(num: int) -> bool:
    """ Return True if num is a pandigital number. Otherwise, return False.
    Assume num is a positive integer.
    >>> is_pandigital(123456789)
    True
    
    """
    num_as_string = str(num)
    if len(num_as_string) == 9:
        for i in range