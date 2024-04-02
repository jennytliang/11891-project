from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Do not include these tokens in the code: if not numbers :
	"""
    rolling_max_list = []
    if numbers:
        rolling_max_list.append(numbers[0])
        for i in range(1, len(numbers)):
            rolling_max_list.append(max(rolling_max_list[i - 1], numbers[i]))
    return rolling_max_list


def find_sum(numbers: List[int], target_sum: int) -> Tuple[int, int]:
    """ From a given list of integers, find two numbers from the list that sum up to the given target_sum.
    If there are no two numbers that sum up to the target_sum, return (-1, -1).
    >>> find_sum([2, 7, 11, 15], 9)
    (2, 7)
    >>> find_sum([2, 7, 11, 15], 30)
    (11, 15)
    >>> find_sum([2, 7, 11, 15], 26)
    (-1, -1)
    
	Do not include these tokens in the code: if not numbers :
	"""
    if numbers:
        if len(numbers) < 2:
            return (-1, -1)
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target_sum:
                    return (numbers[i], numbers[j])
    return (-1, -1)


def find_min_and_max(numbers: List[int]) -> Tuple[int, int]:
    """ From a given list of integers, find the minimum and maximum element in the list.
    If the input list is empty, return (-1, -1).
    >>> find_min_and_max([2, 7, 11, 15])
    (2, 15)
    
	Do not include these tokens in the code: if not numbers :
	"""
    if numbers:
        return (min(numbers), max(numbers))
    return (-1