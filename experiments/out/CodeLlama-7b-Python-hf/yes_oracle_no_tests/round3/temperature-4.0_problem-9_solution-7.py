from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [ max ( numbers [ :( i + 1
	Do not include these tokens in the code: result = []
	"""
    result: List[int] = []
    for i in range(len(numbers)):
        result.append(max(numbers[:i + 1]))
    return result


def rolling_max_tuple(numbers: List[int]) -> List[Tuple[int, int]]:
    """ From a given list of integers, generate a list of tuples (index, max value) for each index in the
    sequence.
    
    >>> rolling_max_tuple([1, 2, 3, 2, 3, 4, 2])
    [(0, 1), (1, 2), (2, 3), (3, 3), (4, 3), (5, 4), (6, 4)]
    
    Include these tokens in the code: return [(i, max ( numbers [ :( i + 1
    Do not include these tokens in the code: result = []
    """
    result: List[Tuple[int, int]] = []
    for i in range(len(numbers)):
        result.append((i, max(numbers[:i + 1])))
    return result


def rolling_max_tuple_comprehension(numbers: List[int]) -> List[Tuple[int, int]]:
    """ From a given list of integers, generate a list of tuples (index, max value) for each index in the
    sequence.
    
    >>> rolling_max_tuple_comprehension([1, 2, 3, 2, 3, 4, 2])
    [(0, 1), (1, 2), (2, 3), (3, 3), (4, 3), (5, 4), (6, 4)]
    
    Include these tokens in the code: return [(i, max ( numbers [ :( i + 1
    Do not include these tokens in the code: result = []
    """
    return [(i, max(numbers[:i + 1])) for i in range(len(numbers))]


def rolling_max_tuple_comprehension_no_index(numbers: List[int]) -> List[Tu