from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: size = len ( numbers )
	"""
    if not numbers:
        return []
    result = [numbers[0]]
    for i in range(1, len(numbers)):
        result.append(max(numbers[i], result[i - 1]))
    return result


def rolling_max_tuple(numbers: List[int]) -> List[Tuple[int, int]]:
    """ From a given list of integers, generate a list of tuples of rolling maximum element found until given
    moment in the sequence and the index of the element in the sequence.
    >>> rolling_max_tuple([1, 2, 3, 2, 3, 4, 2])
    [(1, 0), (2, 1), (3, 2), (3, 3), (4, 4), (4, 5)]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: size = len ( numbers )
	"""
    if not numbers:
        return []
    result = [(numbers[0], 0)]
    for i in range(1, len(numbers)):
        result.append((max(numbers[i], result[i - 1][0]), i))
    return result


def rolling_min(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling minimum element found until given moment
    in the sequence.
    >>> rolling_min([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 2, 2, 3, 3, 2]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: size = len ( numbers )
	"""
    if not numbers:
        return []
    result = [numbers[0]]
    for i in range(1, len(numbers)):
        result.append(min(numbers[i], result[i - 1]))
    return result


def rolling_min_tuple(numbers: List[int]) -> List[Tuple[int, int]]:
    """ From a given list