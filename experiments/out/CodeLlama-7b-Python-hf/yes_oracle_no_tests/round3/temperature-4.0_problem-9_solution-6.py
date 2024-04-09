from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: [ :(
	Do not include these tokens in the code: [:
	"""

    return [max(nu) for nu in zip(numbers, numbers[1:], numbers[2:], numbers[3:], numbers[4:], numbers[5:], numbers[6:])]


def rolling_sum(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum of elements found until given moment in the sequence.
    >>> rolling_sum([1, 2, 3, 2, 3, 4, 2])
    [1, 3, 6, 8, 10, 14, 16]
    
	Include these tokens in the code: [ :(
	Do not include these tokens in the code: [:
	"""

    return [sum(nu) for nu in zip(numbers, numbers[1:], numbers[2:], numbers[3:], numbers[4:], numbers[5:], numbers[6:])]


def rolling_median(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling median of elements found until given moment in the sequence.
    >>> rolling_median([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 2, 2, 2, 3, 3]
    
	Include these tokens in the code: [ :(
	Do not include these tokens in the code: [:
	"""

    return [sorted(nu)[len(nu) // 2] for nu in zip(numbers, numbers[1:], numbers[2:], numbers[3:], numbers[4:], numbers[5:], numbers[6:])]


def rolling_mean(numbers: List[int]) -> List[float]:
    """ From a given list of integers, generate a list of rolling mean of elements found until given moment in the sequence.
    >>> rolling_mean([1, 2, 3, 2, 3, 4, 2])
    [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 3