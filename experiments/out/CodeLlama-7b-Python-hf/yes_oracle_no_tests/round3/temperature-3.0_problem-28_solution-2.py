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


def add_numbers(nums: List[int]) -> int:
    """ Add all numbers in the list together

	Include these tokens in the code: return sum ( nums )
    >>> add_numbers([1, 2, 3])
    6
    >>> add_numbers([4, 5, 6, 7])
    22
    
    """
    return sum(nums)


def concatenate_strings(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string

	Include these tokens in the code: return " ".join ( strings )
    >>> concatenate_strings([])
    ''
    >>> concatenate_strings(['a', 'b', 'c'])
    'a b c'
    
    """
    return " ".join(strings)


def is_prime(num: int) -> bool:
    """ Check if a number is prime
	
	Include these tokens in the code: if num == 1: return False
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(10)
    False
    >>> is_prime(11)
    True
    
    """
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def is_sorted(nums: List[int]) -> bool:
    """ Check if a list of numbers is sorted

	Include these tokens in the code: if nums [ 0 ] >= nums [ - 1 ]: return True
    >>> is_sorted([1, 2, 3])
    True
    >>> is_sorted([1, 2, 5])
    False
    >>> is_sorted([1, 1, 1])
    True
    
    """
    if nums[0] >= nums[-1]:
        return True
    return False


def is_anagram(string1: str, string2: str) -> bool