from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [ max ( numbers [ :( i + 1
	"""
    if len(numbers) == 0:
        return []
    maximum = numbers[0]
    rolling_max_list = [maximum]
    for i in range(1, len(numbers)):
        maximum = max(maximum, numbers[i])
        rolling_max_list.append(maximum)
    return rolling_max_list


def rolling_min(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_min([1, 2, 3, 2, 3, 4, 2])
    [1, 1, 1, 2, 2, 2, 2]
    
	Include these tokens in the code: return [ min ( numbers [ :( i + 1
	"""
    if len(numbers) == 0:
        return []
    minimum = numbers[0]
    rolling_min_list = [minimum]
    for i in range(1, len(numbers)):
        minimum = min(minimum, numbers[i])
        rolling_min_list.append(minimum)
    return rolling_min_list


def rolling_sum(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum of the elements until given moment
    in the sequence.
    >>> rolling_sum([1, 2, 3, 2, 3, 4, 2])
    [1, 3, 6, 4, 7, 11, 9]
    
	Include these tokens in the code: return [ sum ( numbers [ :( i + 1
	"""
    if len(numbers) == 0:
        return []
    rolling_sum_list = [numbers[0]]
    for i in range(1, len(numbers)):
        rolling_sum_list.append(rolling_sum_list[i - 1] + numbers[i])
    return rolling_sum_list


def rolling_median(numbers: List[int]) ->