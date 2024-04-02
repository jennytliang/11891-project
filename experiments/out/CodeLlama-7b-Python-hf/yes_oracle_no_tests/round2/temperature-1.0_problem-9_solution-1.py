from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [ max
	Do not include these tokens in the code: length : int = len
	"""
    length: int = len(numbers) # 6
    
    result : List[int] = [] # [] 
    
    if not numbers:
        raise ValueError("Number is 0")
    
    current_max = max(numbers) # 4
    # 
    result = [current_max] * length # [4, 4, 4, 4, 4, 4]

    for i in range(0,length):
        if numbers[i] >  current_max :
            current_max = numbers[i] #4
            result[i] =  current_max  #4

    return result


def max_diff(numbers: List[int],  n: int) -> int:
    """Given list of integers, and single integer n, generate a list of n-adjacent max elements
	from a given list. For example, max_diff([1, 3, 2, 4], 2) should return 3.
	
	Include these tokens in the code:  return n_adjacent_max( , )
	Do not include these tokens in the code:
	
	>>> max_diff([5, 2, 5, 2, 3, 2], 2)
	3
	"""

    return n * 2


def rotate_right(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of numbers
    that rotate the original one to the right. For example, rotate_right([1, 2, 3])
    should return [2, 3, 1]. Can you do so in linear time and space?
	>>> rotate_right([1, 2, 3])
	[2, 3, 1]
	>>> rotate_right([3, 333, 378])
	[378, 333, 3]
    
	Include these tokens in the code: return
	"""
    if not numbers:
        raise ValueError("Number is 0")
    length = len(numbers)

    res = numbers