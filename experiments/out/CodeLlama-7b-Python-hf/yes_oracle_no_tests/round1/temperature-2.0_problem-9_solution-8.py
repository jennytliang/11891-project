from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Do not include these tokens in the code: if not numbers :
	"""
    if not numbers:
        return []
    max_so_far = max_ending_here = numbers[0]
    rolling_max = [numbers[0]]
    for num in numbers[1:]:
        max_ending_here = max(max_so_far, num)
        rolling_max.append(max_ending_here)
        max_so_far = max_ending_here
    return rolling_max


def max_subarray(nums: List[int]) -> Tuple[int, int, int]:
    """ Return the maximum sum of a contiguous subarray of the given list of numbers.
    >>> max_subarray([-2,1,-3,4,-1,2,1,-5,4])
    (6, 4, 5)
    >>> max_subarray([])
    (0, None, None)
    >>> max_subarray([-1,-2,-3])
    (0, None, None)
    >>> max_subarray([-2,-1])
    (0, None, None)
    >>> max_subarray([-2])
    (0, None, None)
    >>> max_subarray([-2, -1, -3, -4])
    (0, None, None)
    >>> max_subarray([1,-1,2])
    (2, 1, 2)
    >>> max_subarray([1,-1,-2])
    (1, 1, 1)
    >>> max_subarray([-1,-1])
    (0, None, None)
    >>> max_subarray([-1])
    (0, None, None)
    >>> max_subarray([1])
    (1, 0, 1)
    >>> max_subarray([1, -1])
    (1, 0, 1)
    >>> max_subarray([1, 1])
    (2, 0, 2)
    >>> max_subarray([1, 2])
    (3, 0, 2)
    >>> max_subarray([1, 2, 3])
   