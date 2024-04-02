from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: max _ so _ far : List
	"""
    result: List[int] = []
    rolling_max_so_far: List[int] = [numbers[0]]

    for number in numbers[1:]:
        if number > rolling_max_so_far[-1]:
            rolling_max_so_far.append(number)
        else:
            rolling_max_so_far.append(rolling_max_so_far[-1])

    return rolling_max_so_far


def rolling_min(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling minimum element found until given moment
    in the sequence.
    >>> rolling_min([1, 2, 3, 2, 3, 4, 2])
    [1, 1, 1, 2, 2, 2, 2]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: min _ so _ far : List
	"""
    result: List[int] = []
    rolling_min_so_far: List[int] = [numbers[0]]

    for number in numbers[1:]:
        if number < rolling_min_so_far[-1]:
            rolling_min_so_far.append(number)
        else:
            rolling_min_so_far.append(rolling_min_so_far[-1])

    return rolling_min_so_far


def moving_average(numbers: List[int]) -> List[float]:
    """ From a given list of integers, generate a list of moving average elements until given moment in the sequence.
    >>> moving_average([1, 2, 3, 2, 3, 4, 2])
    [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 3.0]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: _ _ _ _ _
	"""
    result: List[float] = []
    _sum: int