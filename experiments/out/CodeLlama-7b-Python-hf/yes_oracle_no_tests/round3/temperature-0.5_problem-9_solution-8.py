from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: [ :(
	Do not include these tokens in the code: [:
	"""

    return [max(nu) for nu in zip(*[numbers[i:] for i in range(len(numbers))])]


def rolling_max_tuple(numbers: List[int]) -> List[Tuple[int, int]]:
    """ From a given list of integers, generate a list of tuples of rolling maximum element and its index found
    until given moment in the sequence.
    >>> rolling_max_tuple([1, 2, 3, 2, 3, 4, 2])
    [(1, 0), (2, 1), (3, 2), (3, 3), (4, 5), (4, 6)]
    
	Include these tokens in the code: [ :(
	Do not include these tokens in the code: [:
	"""

    return [(max(nu), nu.index(max(nu))) for nu in zip(*[numbers[i:] for i in range(len(numbers))])]


def rolling_min(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling minimum element found until given moment
    in the sequence.
    >>> rolling_min([1, 2, 3, 2, 3, 4, 2])
    [1, 1, 2, 2, 2, 2, 2]
    
	Include these tokens in the code: [ :(
	Do not include these tokens in the code: [:
	"""

    return [min(nu) for nu in zip(*[numbers[i:] for i in range(len(numbers))])]


def rolling_min_tuple(numbers: List[int]) -> List[Tuple[int, int]]:
    """ From a given list of integers, generate a list of tuples of rolling minimum element and its index found
    until given moment in the sequence.
    >>> rolling_min_tuple([1, 2, 3, 2, 3, 4, 2])
    [(1, 0), (1, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2