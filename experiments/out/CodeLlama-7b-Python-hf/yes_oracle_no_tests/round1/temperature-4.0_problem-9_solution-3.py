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
    rolling_max_list = []
    # your code here
    for i in range(size):
        if i == 0:
            rolling_max_list.append(numbers[i])
        else:
            rolling_max_list.append(max(rolling_max_list[i - 1], numbers[i]))
    return rolling_max_list


def rolling_min(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling minimum element found until given moment
    in the sequence.
    >>> rolling_min([1, 2, 3, 2, 3, 4, 2])
    [1, 1, 1, 2, 2, 2, 2]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: size = len ( numbers )
	"""
    size = len(numbers)
    rolling_min_list = []
    # your code here
    for i in range(size):
        if i == 0:
            rolling_min_list.append(numbers[i])
        else:
            rolling_min_list.append(min(rolling_min_list[i - 1], numbers[i]))
    return rolling_min_list


def max_min(numbers: List[int]) -> List[Tuple[int, int]]:
    """ From a given list of integers, generate a list of tuples (max, min) found until given moment
    in the sequence.
    >>> max_min([1, 2, 3, 2, 3, 4, 2])
    [(1, 1), (2, 1), (3, 2), (3, 2), (3, 2), (4, 2), (4, 2)]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: size = len ( numbers )
	"""
    size = len(numbers)
    max_min_list = []
    # your code here
    for