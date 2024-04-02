from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    
	Include these tokens in the code: , p
	"""

    pass


def max_min(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a maximum and a minimum of all the integers in a list.
    Empty maximum should be equal to None and empty minimum should be equal to None.
    >>> max_min([])
    (None, None)
    >>> max_min([1, 2, 3, 4])
    (4, 1)
    
	Include these tokens in the code: , p
	"""

    pass


def reverse_and_concatenate(string: str) -> str:
    """ For a given string, return its reverse and its concatenation with itself.
    >>> reverse_and_concatenate("abc")
    'cbaabc'
    
	Include these tokens in the code: , p
	"""

    pass


def count_substring(string: str, substring: str) -> int:
    """ For a given string and a substring, return a count of substrings occurrence in a given string.
    >>> count_substring("123455555555", "55")
    4
    >>> count_substring("12345", "55")
    0
    
	Include these tokens in the code: , p
	"""

    pass


def count_substring_with_step(string: str, substring: str, step: int = 1) -> int:
    """ For a given string, a substring and a step, return a count of substrings occurrence in a given string with a given step.
    >>> count_substring_with_step("123455555555", "55", 2)
    2
    
	Include these tokens in the code: , p
	"""

    pass


def is_prime(n: int) -> bool:
    """ For a given integer n, return True if n is a prime number, False otherwise.
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
   