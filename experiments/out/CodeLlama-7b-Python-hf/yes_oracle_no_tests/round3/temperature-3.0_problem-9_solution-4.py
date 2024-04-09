from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: numbers [ :( i + 1
	Do not include these tokens in the code: nu
	"""


    return _rolling_max_loop(numbers, 0, len(numbers))


def _rolling_max_loop(numbers: List[int], i: int, j: int) -> List[int]:
    if i >= j:
        return [numbers[i]]
    else:
        return [numbers[i]] + _rolling_max_loop(numbers, i + 1, j)


def _rolling_max_rec(numbers: List[int], i: int, j: int) -> List[int]:
    if i >= j:
        return [numbers[i]]
    else:
        return [max(numbers[i], numbers[j])] + _rolling_max_rec(numbers, i + 1, j)


def rolling_max_rec(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: numbers [ :( i + 1
	Do not include these tokens in the code: nu
	"""

    return _rolling_max_rec(numbers, 0, len(numbers))


def rolling_max_tuple(numbers: List[int]) -> List[Tuple[int, int]]:
    """ From a given list of integers, generate a list of tuples (i, max_element). The first tuple should
    be (0, numbers[0]) and the last tuple should be (len(numbers) - 1, numbers[len(numbers) - 1]).
    >>> rolling_max_tuple([1, 2, 3, 2, 3, 4, 2])
    [(0, 1), (1, 2), (2, 3), (3, 3), (4, 3), (5, 4), (6, 4)]
    
	Include these tokens in the code: numbers [ :( i