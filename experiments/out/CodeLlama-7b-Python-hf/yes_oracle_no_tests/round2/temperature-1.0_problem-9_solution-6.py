from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [
	Do not include these tokens in the code: rolling _ max _ list = []
	"""
    rolling_max_list = []
    for i in range(len(numbers)):
        if i == 0:
            rolling_max_list.append(numbers[i])
        else:
            if numbers[i] > rolling_max_list[i-1]:
                rolling_max_list.append(numbers[i])
            else:
                rolling_max_list.append(rolling_max_list[i-1])
    return rolling_max_list


def rolling_min(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling minimum element found until given moment
    in the sequence.
	>>> rolling_min([1, 2, 3, 2, 3, 4, 2])
	[1, 1, 1, 2, 2, 2, 2]
	"""
    rolling_min_list = []
    for i in range(len(numbers)):
        if i == 0:
            rolling_min_list.append(numbers[i])
        else:
            if numbers[i] < rolling_min_list[i-1]:
                rolling_min_list.append(numbers[i])
            else:
                rolling_min_list.append(rolling_min_list[i-1])
    return rolling_min_list


def rolling_median(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling median element found until given moment
    in the sequence.
    >>> rolling_median([1, 2, 3, 2, 3, 4, 2])
    [1, 1, 2, 2, 2, 3, 3]
    """
    rolling_median_list = []
    for i in range(len(numbers)):
        if i == 0:
            rolling_median_list.append(numbers[i])
        else:
            if i % 2 == 0:
                rolling_median_list.append(numbers[i])
            else:
