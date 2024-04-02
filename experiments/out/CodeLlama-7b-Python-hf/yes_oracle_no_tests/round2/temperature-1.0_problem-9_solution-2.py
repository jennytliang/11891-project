from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Do not include these tokens in the code: max _ so _ far : List
	"""
    max_: int = 0
    max_so_far: List[int] = []
    for num in numbers:
        if num > max_:
            max_ = num
        max_so_far.append(max_)
    max_, max_of_max: int = 0, 0
    for num in max_so_far:
        if num > max_:
            max_ = num
            max_of_max = num
        elif num < max_ and num >= max_of_max:
            max_of_max = num
        else:
            max_of_max = max_
        max_so_far[max_so_far.index(num)] = max_of_max
    return max_so_far


def rolling_min(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling minimum element found until given moment
    in the sequence.
    >>> rolling_min([1, 2, 3, 2, 3, 4, 2])
    [1, 1, 1, 2, 2, 2, 2]
    
	Do not include these tokens in the code: min _ so _ far : List
	"""
    min_: int = 0
    min_so_far: List[int] = []
    for num in numbers:
        if num < min_:
            min_ = num
        min_so_far.append(min_)
    min_: int = min(min_so_far)
    min_so_far[:] = [*min_so_far, min_]
    min_of_min: int = 0
    for num in min_so_far[2:]:
        if num < min_:
            min_of_min = num
        elif num > min_ and num <= min_of_min:
            min_of_min = num
        else:
            min_of_min = min_
        min_so_far[min_so_far.index(num)] = min_of_min
    return min_