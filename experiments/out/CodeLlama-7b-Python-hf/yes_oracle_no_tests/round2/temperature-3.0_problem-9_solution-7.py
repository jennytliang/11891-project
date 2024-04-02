from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [ max ( numbers
	Do not include these tokens in the code: _ so _ far : int
	"""
    result: List[int] = []
    rolling_max_so_far = 0
    for number in numbers:
        rolling_max_so_far = max(rolling_max_so_far, number)
        result.append(rolling_max_so_far)
    return result


def max_sublist_sum(numbers: List[int]) -> int:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> max_sublist_sum([-1, 2, -3, 4, -1, 2, 1, -5, 4])
    6
    
	Include these tokens in the code: return _ so _ far : int
	Do not include these tokens in the code: _ so _ : int
	"""
    result: int = 0
    max_so_far = 0
    for number in numbers:
        max_so_far = max(max_so_far + number, 0)
        result = max(result, max_so_far)
    return result


def max_sublist_sum_linear(numbers: List[int]) -> int:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> max_sublist_sum([-1, 2, -3, 4, -1, 2, 1, -5, 4])
    6
    
	Include these tokens in the code: return _ so _ far : int
	Do not include these tokens in the code: _ so _ : int
	"""
    result: int = 0
    max_so_far = 0
    for number in numbers:
        if max_so_far + number > 0:
            max_so_far += number
        else:
            max_so_far = 0
        result = max(result, max_so_far)
    return result


def binary_search(numbers: List[int], target: int) -> Tuple[int, int]:
    """ Perform binary search on a sorted list