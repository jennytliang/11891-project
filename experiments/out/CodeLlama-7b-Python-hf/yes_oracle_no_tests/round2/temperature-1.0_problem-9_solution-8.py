from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Do not include these tokens in the code: #
	"""
    rolling_max_list: List[int] = []
    max_number = 0
    for number in numbers:
        if number > max_number:
            max_number = number
        rolling_max_list.append(max_number)
    return rolling_max_list


def rolling_min(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling minimum element found until given moment
    in the sequence.
    >>> rolling_min([1, 2, 3, 2, 3, 4, 2])
    [1, 1, 1, 2, 2, 2, 2]
    
	Do not include these tokens in the code: #
	"""
    rolling_min_list: List[int] = []
    min_number = 0
    for number in numbers:
        if number < min_number:
            min_number = number
        rolling_min_list.append(min_number)
    return rolling_min_list


def rolling_median(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling median element found until given moment
    in the sequence.
    >>> rolling_median([1, 2, 3, 2, 3, 4, 2])
    [1, 1, 2, 2, 2, 2, 3]
    
	Do not include these tokens in the code: #
	"""
    rolling_median_list: List[int] = []
    numbers_len = len(numbers)
    for i in range(numbers_len):
        numbers_copy_left = numbers[:i]
        numbers_copy_right = numbers[i + 1:]
        numbers_copy_right.append(numbers[i])
        median = (sum(numbers_copy_left) + sum(numbers_copy_right)) / 2
        rolling_median_list.append(median)
    return rolling_median_list


def rolling_average(numbers: List