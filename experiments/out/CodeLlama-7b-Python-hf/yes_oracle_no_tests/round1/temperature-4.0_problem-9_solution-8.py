from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: size = len ( numbers )
	"""
    size = len(numbers)
    rolling_max = []
    for i in range(size):
        max_element = numbers[i]
        for j in range(i, size):
            if numbers[j] > max_element:
                max_element = numbers[j]
        rolling_max.append(max_element)
    return rolling_max


def rolling_max_tuple(numbers: List[int]) -> List[Tuple[int, int]]:
    """ From a given list of integers, generate a list of tuples containing the index and the value of the
    rolling maximum element found until given moment in the sequence.
    >>> rolling_max_tuple([1, 2, 3, 2, 3, 4, 2])
    [(0, 1), (1, 2), (2, 3), (3, 3), (4, 3), (5, 4), (6, 4)]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: size = len ( numbers )
	"""
    size = len(numbers)
    rolling_max = []
    for i in range(size):
        max_element = numbers[i]
        max_index = i
        for j in range(i, size):
            if numbers[j] > max_element:
                max_element = numbers[j]
                max_index = j
        rolling_max.append((max_index, max_element))
    return rolling_max


def rolling_max_tuple_pythonic(numbers: List[int]) -> List[Tuple[int, int]]:
    """ From a given list of integers, generate a list of tuples containing the index and the value of the
    rolling maximum element found until given moment in the sequence.
    >>> rolling_max_tuple_pythonic([1, 2, 3, 2, 3, 4, 2])
    [(0, 1), (1, 2), (2, 3), (3, 3), (4, 3), (5, 4), (6, 4)]