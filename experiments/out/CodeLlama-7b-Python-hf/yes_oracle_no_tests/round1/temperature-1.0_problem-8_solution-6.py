from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    
	Include these tokens in the code: s , p =
	"""
    pass


def maximum_odds(numbers: List[int]) -> int:
    """ For a given array of numbers return the missing number between 1 and 31 in the array. 
    The array contains 30 positive integers between 1 and 30 with no repeated numbers.
    
    >>> maximum_odds([3,7,10,20,27])
    1
    >>> maximum_odds([3,7,10,21,27])
    20
    
    Write your code below this row 👇
    """
    s = 1
    for num in numbers:
        s ^= num
    
    for i in range(1, 31):
        if (s >> i) & 1 == 1:
            return i
    
    return 0


def minimum_even(numbers: List[int]) -> int:
    """ For a given array of numbers, return a first missing positive integer that does not appear in array. Return number is not defined first (input == []).
    The array contains non-negative integers. The element can appear more than once in the array.
    
    >>> minimum_even([3,2,1,3])
    2
    >>> minimum_even([2,2])
    1
    
    You can use this tokens in your code: value = numbers.index(minimum_even)
    """
    pass
