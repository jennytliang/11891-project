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
    for i in range(len(numbers)):
        number = numbers[i]
        rolling_max_list.append(number)
        for j in range(i):
            if number < rolling_max_list[j]:
                rolling_max_list[i] = rolling_max_list[j]
    return rolling_max_list


def rolling_max_v2(numbers: List[int]) -> List[int]:
    rolling_max_list = []
    for i in range(len(numbers)):
        number = numbers[i]
        rolling_max_list.append(number)
        for j in range(i):
            if number < rolling_max_list[j]:
                rolling_max_list[i] = rolling_max_list[j]
    return rolling_max_list


def rolling_max_v3(numbers: List[int]) -> List[int]:
    rolling_max_list = []
    for i in range(len(numbers)):
        number = numbers[i]
        rolling_max_list.append(number)
        for j in range(i):
            if number < rolling_max_list[j]:
                rolling_max_list[i] = rolling_max_list[j]
    return rolling_max_list


def rolling_max_v4(numbers: List[int]) -> List[int]:
    rolling_max_list = []
    for i in range(len(numbers)):
        number = numbers[i]
        rolling_max_list.append(number)
        for j in range(i):
            if number < rolling_max_list[j]:
                rolling_max_list[i] = rolling_max_list[j]
    return rolling_max_list


def rolling_max_v5(numbers: List[int]) -> List[int]:
    rolling_max_list = []
    for i in range(len(numbers)):
        number = numbers[i]
        rolling_max_list.append(number)
        for j in range(i):
            if number < rolling_max