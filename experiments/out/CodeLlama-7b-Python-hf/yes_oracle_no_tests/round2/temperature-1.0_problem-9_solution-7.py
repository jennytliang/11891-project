from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [
	Do not include these tokens in the code: max _ so _ far = numbers
	"""
    return [max(numbers[:i]) for i in range(1, len(numbers) + 1)]


def rolling_min(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling minimum element found until given moment
    in the sequence.
    >>> rolling_min([1, 2, 3, 2, 3, 4, 2])
    [1, 1, 1, 2, 2, 2, 2]
    
	Include these tokens in the code: return [
	Do not include these tokens in the code: min _ so _ far = numbers
	"""
    return [min(numbers[:i]) for i in range(1, len(numbers) + 1)]


def moving_average(numbers: List[int], k: int) -> List[float]:
    """ From a given list of integers, generate a list of rolling average element found until given moment
    in the sequence.
    >>> moving_average([1, 2, 3, 4, 3, 2, 1], 3)
    [1.0, 1.5, 2.0, 2.5, 2.0, 1.5, 1.0]
    
	Include these tokens in the code: return [
	Do not include these tokens in the code: sum _ so _ far = numbers
	"""
    return [sum(numbers[:i]) / i for i in range(1, len(numbers) + 1)]


def moving_median(numbers: List[int], k: int) -> List[float]:
    """ From a given list of integers, generate a list of rolling median element found until given moment
    in the sequence.
    >>> moving_median([1, 2, 3, 4, 3, 2, 1], 3)
    [1.0, 2.0, 3.0, 3.0, 3.0, 3.0, 2.0]
    
	Include these tokens in the code: return [
	Do not include these tokens