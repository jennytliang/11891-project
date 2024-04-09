from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [
	Do not include these tokens in the code: size = len ( numbers )
	"""
    rolling_max = []
    for i in range(len(numbers)):
        if i == 0:
            rolling_max.append(numbers[0])
        else:
            rolling_max.append(max(rolling_max[i-1], numbers[i]))
    return rolling_max


def rolling_max2(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max2([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [
	Do not include these tokens in the code: size = len ( numbers )
	"""
    rolling_max = []
    for i in range(len(numbers)):
        if i == 0:
            rolling_max.append(numbers[0])
        else:
            if numbers[i] > rolling_max[i-1]:
                rolling_max.append(numbers[i])
            else:
                rolling_max.append(rolling_max[i-1])
    return rolling_max


def min_max_sum(numbers: List[int]) -> Tuple[int, int, int]:
    """ From a given list of integers, return a tuple of (min, max, sum) of the values.
    >>> min_max_sum([1, 2, 3, 4, 5])
    (1, 5, 15)
    >>> min_max_sum([-1, -2, -3, -4, -5])
    (-5, -1, -15)
    
	Include these tokens in the code: min_number = max_number = numbers[0]
	"""
    min_number = max_number = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] < min_number:
            min_number = numbers[i]
        if numbers[