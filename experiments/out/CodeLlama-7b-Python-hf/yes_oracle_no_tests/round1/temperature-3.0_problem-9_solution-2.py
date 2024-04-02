from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [
	Do not include these tokens in the code: rolling _
	"""
    rolling_max_list = []
    for index, element in enumerate(numbers):
        if index == 0:
            rolling_max_list.append(element)
        else:
            rolling_max_list.append(max(rolling_max_list[index - 1], element))
    return rolling_max_list


def rolling_min(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling minimum element found until given moment
    in the sequence.
    >>> rolling_min([1, 2, 3, 2, 3, 4, 2])
    [1, 1, 1, 2, 2, 2, 2]
    
	Include these tokens in the code: return [
	Do not include these tokens in the code: rolling _
	"""
    rolling_min_list = []
    for index, element in enumerate(numbers):
        if index == 0:
            rolling_min_list.append(element)
        else:
            rolling_min_list.append(min(rolling_min_list[index - 1], element))
    return rolling_min_list


def rolling_median(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling median element found until given moment
    in the sequence.
    >>> rolling_median([1, 2, 3, 2, 3, 4, 2])
    [1, 1, 2, 2, 2, 3, 3]
    
	Include these tokens in the code: return [
	Do not include these tokens in the code: rolling _
	"""
    rolling_median_list = []
    for index, element in enumerate(numbers):
        if index == 0:
            rolling_median_list.append(element)
        else:
            value = sorted(rolling_median_list[index - 1:index + 1])
            if len(value) % 2 == 0:
                rolling_median_list.append