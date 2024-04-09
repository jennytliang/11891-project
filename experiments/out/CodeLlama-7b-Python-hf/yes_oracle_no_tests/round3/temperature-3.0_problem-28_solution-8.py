from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    
	Include these tokens in the code: return " ". join ( strings )
	"""
    return " ".join(strings)


def count_even(numbers: List[int]) -> int:
    """ Count even numbers in a list of numbers
    >>> count_even([2, 1, 2, 3, 4])
    2
    >>> count_even([1, 3, 5])
    0
    
	Include these tokens in the code: return len ( [ x for x in numbers if x % 2 == 0 ] )
	"""
    return len([x for x in numbers if x % 2 == 0])


def even_or_odd(number: int) -> str:
    """ Check if number is even or odd
    >>> even_or_odd(2)
    'even'
    >>> even_or_odd(5)
    'odd'
    
	Include these tokens in the code: if number % 2 == 0 else return 'odd'
	"""
    return "even" if number % 2 == 0 else "odd"


def increment_list_values(numbers: List[int]) -> List[int]:
    """ Increment all list values
    >>> increment_list_values([1, 2, 3, 4])
    [2, 3, 4, 5]
    
	Include these tokens in the code: return [x + 1 for x in numbers]
	"""
    return [x + 1 for x in numbers]


def is_even(number: int) -> bool:
    """ Check if number is even
    >>> is_even(2)
    True
    >>> is_even(3)
    False
    
	Include these tokens in the code: return number % 2 == 0
	"""
    return number % 2 == 0


def is_leap_year(year: int) -> bool:
    """ Check if a year is a leap year
    >>> is_leap_year(2020)
    True
    >>> is_leap_year(2021)
    False
    
	Include these tokens in the code: if year % 4