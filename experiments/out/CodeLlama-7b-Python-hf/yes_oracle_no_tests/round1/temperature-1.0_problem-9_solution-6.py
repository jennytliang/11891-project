from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: max _ so _ far = numbers
	"""
    rolling_max_list = []
    for number in numbers:
        if len(rolling_max_list) == 0:
            rolling_max_list.append(number)
        else:
            rolling_max_list.append(max(rolling_max_list[-1], number))
    return rolling_max_list


def rolling_min(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling minimum element found until given moment
    in the sequence.
    >>> rolling_min([1, 2, 3, 2, 3, 4, 2])
    [1, 1, 1, 2, 2, 2, 2]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: min _ so _ far = numbers
	"""
    rolling_min_list = []
    for number in numbers:
        if len(rolling_min_list) == 0:
            rolling_min_list.append(number)
        else:
            rolling_min_list.append(min(rolling_min_list[-1], number))
    return rolling_min_list


def rolling_sum(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum until given moment in the sequence.
    >>> rolling_sum([1, 2, 3, 2, 3, 4, 2])
    [1, 3, 6, 5, 8, 12, 10]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: sum _ so _ far = numbers
	"""
    rolling_sum_list = []
    for number in numbers:
        if len(rolling_sum_list) == 0:
            rolling_sum_list.append(number)
        else:
            rolling_sum_list.append(rolling_sum_list[-1] + number)
    return rolling_sum_list


def rolling_median(numbers: List[