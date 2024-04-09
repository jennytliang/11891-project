from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [
	Do not include these tokens in the code: rolling _
	"""
    return [max(numbers[:i + 1]) for i in range(len(numbers))]


def rolling_min(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling minimum element found until given moment
    in the sequence.
    >>> rolling_min([1, 2, 3, 2, 3, 4, 2])
    [1, 1, 1, 2, 2, 2, 2]

	Include these tokens in the code: return [
	Do not include these tokens in the code: rolling _
	"""
    return [min(numbers[:i + 1]) for i in range(len(numbers))]


def rolling_sum(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum until given moment in the sequence.
    >>> rolling_sum([1, 2, 3, 2, 3, 4, 2])
    [1, 3, 6, 8, 10, 14, 12]

	Include these tokens in the code: return [
	Do not include these tokens in the code: rolling _
	"""
    return [sum(numbers[:i + 1]) for i in range(len(numbers))]


def rolling_median(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling median until given moment in the sequence.
    >>> rolling_median([1, 2, 3, 2, 3, 4, 2])
    [1, 1, 2, 2, 2, 2, 2]

	Include these tokens in the code: return [
	Do not include these tokens in the code: rolling _
	"""
    return [median(numbers[:i + 1]) for i in range(len(numbers))]


def median(numbers: List[int]) -> int:
    """ Calculate median of a given list of integers.
    >>> median([1, 2, 3