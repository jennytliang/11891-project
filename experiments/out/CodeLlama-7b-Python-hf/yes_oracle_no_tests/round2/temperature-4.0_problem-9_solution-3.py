from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [ max
	Do not include these tokens in the code: size = len
	"""
    size = len(numbers)
    max_list = [0] * size
    for i in range(size):
        if i == 0:
            max_list[i] = numbers[i]
        else:
            if numbers[i] > max_list[i-1]:
                max_list[i] = numbers[i]
            else:
                max_list[i] = max_list[i-1]
    return max_list


def rolling_max_optimized(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max_optimized([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [ max
	Do not include these tokens in the code: size = len
	"""
    size = len(numbers)
    max_list = [0] * size
    max_list[0] = numbers[0]
    for i in range(1, size):
        if numbers[i] > max_list[i-1]:
            max_list[i] = numbers[i]
        else:
            max_list[i] = max_list[i-1]
    return max_list


def rolling_max_tuple(numbers: List[int]) -> List[Tuple[int, int]]:
    """ From a given list of integers, generate a list of tuples (index, maximum element) found until given moment
    in the sequence.
    >>> rolling_max_tuple([1, 2, 3, 2, 3, 4, 2])
    [(0, 1), (1, 2), (2, 3), (3, 3), (4, 3), (5, 4), (6, 4)]
    
	Include these tokens in the code: return [ (index, max
	Do not include these tokens in the code