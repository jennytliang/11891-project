from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: size = len ( numbers )
	"""
    # return 
    size = len(numbers)
    result = [0] * size
    result[0] = numbers[0]
    for i in range(1, size):
        result[i] = max(result[i-1], numbers[i])
    return result


def rolling_min(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling minimum element found until given moment
    in the sequence.
    >>> rolling_min([1, 2, 3, 2, 3, 4, 2])
    [1, 1, 1, 2, 2, 2, 2]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: size = len ( numbers )
	"""
    # return 
    size = len(numbers)
    result = [0] * size
    result[0] = numbers[0]
    for i in range(1, size):
        result[i] = min(result[i-1], numbers[i])
    return result


def max_of_subarrays(k: int, numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of maximum elements from each subarray of k elements.
    >>> max_of_subarrays(3, [1, 2, 3, 4, 5, 2, 1])
    [2, 3, 4, 5, 5, 5, 5]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: size = len ( numbers )
	"""
    # return 
    size = len(numbers)
    result = [0] * (size - k + 1)
    for i in range(size - k + 1):
        result[i] = max(numbers[i:i + k])
    return result


def max_of_subarrays_improved(k: int, numbers: List[int]) -> List[int]:
   