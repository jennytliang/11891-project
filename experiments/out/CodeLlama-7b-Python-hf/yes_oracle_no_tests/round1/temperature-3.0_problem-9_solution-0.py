from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [
	Do not include these tokens in the code: rolling _
	"""
    rolling_max_list: List[int] = []
    rolling_max_list.append(max(numbers))
    for i in range(1, len(numbers)):
        if numbers[i] > rolling_max_list[i - 1]:
            rolling_max_list.append(numbers[i])
        else:
            rolling_max_list.append(rolling_max_list[i - 1])
    return rolling_max_list


def rolling_min(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling minimum element found until given moment
    in the sequence.
    >>> rolling_min([1, 2, 3, 2, 3, 4, 2])
    [1, 1, 1, 2, 2, 2, 2]
    
	Include these tokens in the code: return [
	Do not include these tokens in the code: rolling _
	"""
    rolling_min_list: List[int] = []
    rolling_min_list.append(min(numbers))
    for i in range(1, len(numbers)):
        if numbers[i] < rolling_min_list[i - 1]:
            rolling_min_list.append(numbers[i])
        else:
            rolling_min_list.append(rolling_min_list[i - 1])
    return rolling_min_list


def rolling_sum(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum found until given moment
    in the sequence.
    >>> rolling_sum([1, 2, 3, 2, 3, 4, 2])
    [1, 3, 6, 4, 7, 11, 9]
    
	Include these tokens in the code: return [
	Do not include these tokens in the code: rolling _
	"""
    rolling_sum_list: List[int] = []
    rolling_sum_list.append(sum(numbers[:2]))
    for i in