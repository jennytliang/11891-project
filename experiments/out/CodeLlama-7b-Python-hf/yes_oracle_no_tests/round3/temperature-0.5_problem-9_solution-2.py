from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: [ :(
	Do not include these tokens in the code: [:
	"""

    return [max(nu) for nu in zip(numbers, numbers[1:], numbers[2:])]


def merge_sort(numbers: List[int]) -> List[int]:
    """
    >>> merge_sort([1, 4, 2, 6, 3, 5, 7, 10, 9, 8])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> merge_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> merge_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
	Include these tokens in the code: [ :(
	Do not include these tokens in the code: [:
	"""
    if len(numbers) < 2:
        return numbers
    mid = len(numbers) // 2
    left = merge_sort(numbers[:mid])
    right = merge_sort(numbers[mid:])
    return merge(left, right)


def merge(left: List[int], right: List[int]) -> List[int]:
    """
    >>> merge([1, 4, 2, 6], [3, 5, 7, 10, 9, 8])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> merge([10, 9, 8, 7], [6, 5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 1