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


def rolling_max_tuple(numbers: List[int]) -> List[Tuple[int, int]]:
    """ From a given list of integers, generate a list of tuples (index, maximum element found until given moment
    in the sequence).
    >>> rolling_max_tuple([1, 2, 3, 2, 3, 4, 2])
    [(0, 1), (1, 2), (2, 3), (3, 3), (4, 3), (5, 4), (6, 4)]
    
	Include these tokens in the code: return [
	Do not include these tokens in the code: rolling _
	"""
    return [(i, max(numbers[:i + 1])) for i in range(len(numbers))]


def rolling_max_tuple_pythonic(numbers: List[int]) -> List[Tuple[int, int]]:
    """ From a given list of integers, generate a list of tuples (index, maximum element found until given moment
    in the sequence).
    >>> rolling_max_tuple_pythonic([1, 2, 3, 2, 3, 4, 2])
    [(0, 1), (1, 2), (2, 3), (3, 3), (4, 3), (5, 4), (6, 4)]
    
	Include these tokens in the code: return [
	Do not include these tokens in the code: rolling _
	"""
    return [(i, max(numbers[:i + 1])) for i in range(len(numbers))]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
