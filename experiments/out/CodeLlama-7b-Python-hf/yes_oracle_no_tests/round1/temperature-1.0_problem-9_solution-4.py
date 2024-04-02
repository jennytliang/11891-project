from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: max _ so _ far : List
	"""
    pass


def rolling_max2(numbers: List[int]) -> List[int]:
    """
	To test your answer, we are going to call a function max_so_far (not in your code) on your list of 
	int numbers. max_so_far should return the highest value encountered in numbers.
	Use this code to generate the answers: max_so_far(rolling_max([1, 2, 3, 2, 3, 4, 2]))
	"""
    pass


def product_except_self(nums: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of products for all sublists excluding the 
    current position. Example for [2, 4, 6, 8] the output should be 
     [1, 8, 8, 4].
    
     Solution (use for loops) 
    	Do not include these tokens in the code: return _[: _[1:]]. reverse : List, reverse _
	Do not include these tokens in the code: _ so _
    """
    pass


def max_product(nums: List[int]) -> int:
    """ From a given list of positive integers, return the maximum product that can be obtained by 
    multiplying 
    4 integers from the list. The answer may be very large (larger than Python has INT).
    """
    pass


def reverse_string(string: str) -> str:
    """ Generate a string in which input string has been reversed.
    Example: 'abc' -> 'cba', 'a' -> 'a', 'aabcc' -> 'ccbaaa' 
    
    Solution (use for loops) 
	For solution, you’re going to need to define a reversed version of a string (i.e.’reversed’) 
	that will take a string as input and then output another string with elements in reverse order.

    You can solve this with a single for loop:
	
    	Do not include these tokens in the code: return _[: _[1:]]. reverse : List, reverse _
	