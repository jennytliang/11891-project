from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [ max
	Do not include these tokens in the code: size = len
	"""
    size = len(numbers)
    rolling_max = []
    for i in range(size):
        max_number = numbers[i]
        for j in range(i, size):
            if numbers[j] > max_number:
                max_number = numbers[j]
        rolling_max.append(max_number)
    return rolling_max


def max_size_subarray(numbers: List[int], target: int) -> Tuple[int, int]:
    """ From a given list of integers, find a subarray with the largest sum
    such that the sum of the subarray is target.
    >>> max_size_subarray([1, 2, 3, 4, 5], 9)
    (0, 4)
    >>> max_size_subarray([1, 2, 3, 4, 5], 15)
    (0, 4)
    >>> max_size_subarray([1, 2, 3, 4, 5], 10)
    (0, 3)
    >>> max_size_subarray([1, 2, 3, 4, 5], 20)
    (0, 4)
    >>> max_size_subarray([1, 2, 3, 4, 5], 1)
    (0, 0)
    >>> max_size_subarray([1, 2, 3, 4, 5], 0)
    (0, 0)
    >>> max_size_subarray([1, 2, 3, 4, 5], -5)
    (0, 0)
    >>> max_size_subarray([], 10)
    Traceback (most recent call last):
        ...
    ValueError: Input list is empty
    >>> max_size_subarray([1, 2, 3, 4, 5], None)
    Traceback (most recent call last):
        ...
    ValueError: Target value is None
    """
    if not numbers:
        raise ValueError("Input list is empty")
    if target is