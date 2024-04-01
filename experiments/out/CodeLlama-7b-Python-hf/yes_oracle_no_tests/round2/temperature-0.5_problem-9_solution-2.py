from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [
	Do not include these tokens in the code: rolling _
	"""
    return [max(numbers[:i+1]) for i in range(len(numbers))]


def max_sublist_sum(numbers: List[int]) -> Tuple[int, int, int]:
    """ From a given list of integers, find the sublist with the maximum sum of its elements.
    >>> max_sublist_sum([-1, 3, -2, 5, 1, -1, 3, 2, 1, -2, 2, 3, -1, 3, -2, -2, 2, 3, -1, -2, -1, -1, -2, 2, -1, 2, 3, -2, 3, -1, -2, -2, 2, 1, -2, -1, 1, -2, -1, -2, 2, 2, -2, -1, -1, -2, 2, 3, -2, 3, -1, -1, 2, -2, 2, 3, -1, -2, 3, -2, 2, -2, 2, 1, -2, -1, 2, -1, 3, -2, 3, -2, -2, 2, 1, -2, -1, 3, -2, 2, -2, 1, -2, 3, -1, -2, 3, -2, -2, 2, 2, -2, -1, -2, 2, -2, 3, -1, -2, 3, -1, 1, -2, -2, 3, -2, 1, -2, -2, 2, 2, -2, 2, 3, -1, -2, 3, -2, -2, 2, -2, 1, -2, -1, 3, -1, 3, -2, -1, -1, -2, 2, 3, -1, -2, -2, 2, -2, -1, -2, 