from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [ max ( numbers [ :( i + 1
	"""
    if len(numbers) == 0:
        return []
    result = []
    for i, n in enumerate(numbers):
        if i == 0:
            result.append(n)
        else:
            result.append(max(result[i - 1], numbers[i]))
    return result


def rolling_max2(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [ max ( numbers [ :( i + 1
    """
    if len(numbers) == 0:
        return []
    result = []
    result.append(max(numbers[0], numbers[1]))
    for i in range(2, len(numbers)):
        result.append(max(numbers[i], result[i - 1]))
    return result


def rolling_max_tuple(numbers: List[int]) -> List[Tuple[int, int]]:
    """ From a given list of integers, generate a list of tuples (index, value) where index is the index of
    the maximum element in the list until the given moment in the sequence.
    >>> rolling_max_tuple([1, 2, 3, 2, 3, 4, 2])
    [(0, 1), (1, 2), (2, 3), (3, 3), (4, 3), (5, 4), (6, 4)]
    
	Include these tokens in the code: return [(i, max ( numbers [ :( i + 1
    """
    if len(numbers) == 0:
        return []
    result = []
    for i, n in enumerate(numbers):
        if i == 0:
            result.append((i, n))
        else:
            result.append((i, max(