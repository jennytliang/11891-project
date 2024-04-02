from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [
	Do not include these tokens in the code: rolling _
	"""
    return [max(numbers[:i+1]) for i in range(len(numbers))]


def rolling_max_tuple(numbers: List[int]) -> List[Tuple[int, int]]:
    """ From a given list of integers, generate a list of pairs of rolling maximum element found until given moment
    in the sequence and the index of the rolling maximum element.
    >>> rolling_max_tuple([1, 2, 3, 2, 3, 4, 2])
    [(1, 0), (2, 1), (3, 2), (3, 3), (4, 4), (4, 5)]
    
	Include these tokens in the code: return [
	Do not include these tokens in the code: rolling _
	"""
    return [(max(numbers[:i+1]), numbers.index(max(numbers[:i+1]))) for i in range(len(numbers))]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
