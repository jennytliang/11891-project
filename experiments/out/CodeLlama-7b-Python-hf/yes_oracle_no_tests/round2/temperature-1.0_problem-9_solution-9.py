from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: max _ so _ far : List
	"""
    return [max(numbers[:i]) for i in range(1, len(numbers) + 1)]


def rolling_max_tuple(numbers: List[int]) -> List[Tuple[int, int]]:
    """ From a given list of integers, generate a list of tuples of rolling maximum element found until given
    moment in the sequence and moment of occurrence.
    >>> rolling_max_tuple([1, 2, 3, 2, 3, 4, 2])
    [(1, 0), (2, 1), (3, 2), (3, 3), (4, 4), (4, 5), (4, 6)]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: max _ so _ far : List
	"""
    return [(max(numbers[:i]), i) for i in range(1, len(numbers) + 1)]


def rolling_max_dict(numbers: List[int]) -> List[Tuple[int, int]]:
    """ From a given list of integers, generate a list of tuples of rolling maximum element found until given
    moment in the sequence and moment of occurrence.
    >>> rolling_max_dict([1, 2, 3, 2, 3, 4, 2])
    [(1, 0), (2, 1), (3, 2), (3, 3), (4, 4), (4, 5), (4, 6)]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: max _ so _ far : List
	"""
    return [(max(numbers[:i]), i) for i in range(1, len(numbers) + 1)]


def rolling_max_dict_2(numbers: List[int]) -> List[Tuple[int, int]]:
    """ From a given list of integers, generate a list of tuples of rolling maximum element found until given
    moment in the sequence and moment of occurrence.
    >>> rolling_max_dict_2([1, 2, 3, 2, 