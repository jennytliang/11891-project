from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: rolling _ max _ so _ far
	"""
    rolling_max_list = []
    rolling_max_so_far = numbers[0]

    for number in numbers:
        rolling_max_so_far = max(rolling_max_so_far, number)
        rolling_max_list.append(rolling_max_so_far)
    return rolling_max_list


def rolling_min(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling minimum element found until given moment
    in the sequence.
    >>> rolling_min([1, 2, 3, 2, 3, 4, 2])
    [1, 1, 1, 2, 2, 2, 2]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: rolling _ min _ so _ far
	"""
    rolling_min_list = []
    rolling_min_so_far = numbers[0]

    for number in numbers:
        rolling_min_so_far = min(rolling_min_so_far, number)
        rolling_min_list.append(rolling_min_so_far)
    return rolling_min_list


def rolling_sum(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum found until given moment
    in the sequence.
    >>> rolling_sum([1, 2, 3, 2, 3, 4, 2])
    [1, 3, 6, 4, 7, 11, 9]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: rolling _ sum _ so _ far
	"""
    rolling_sum_list = []
    rolling_sum_so_far = numbers[0]

    for number in numbers:
        rolling_sum_so_far = rolling_sum_so_far + number
        rolling_sum_list.append(rolling_sum_so_far)
    return rolling_sum_list


def max_min