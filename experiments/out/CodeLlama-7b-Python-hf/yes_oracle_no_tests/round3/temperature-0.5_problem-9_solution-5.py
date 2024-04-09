from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: [ :(
	Do not include these tokens in the code: [:
	"""

    return [max(nu) for nu in zip(numbers, numbers[1:], numbers[2:])]


def get_min_max(numbers: List[int]) -> Tuple[int, int]:
    """ From a given list of integers, return a tuple with the minimum and maximum value found.
    >>> get_min_max([1, 2, 3, 2, 3, 4, 2])
    (1, 4)
    
	Include these tokens in the code: [ :(
	Do not include these tokens in the code: [:
	"""
    return min(numbers), max(numbers)


def get_min_max_tuple(numbers: List[int]) -> Tuple[int, int]:
    """ From a given list of integers, return a tuple with the minimum and maximum value found.
    >>> get_min_max_tuple([1, 2, 3, 2, 3, 4, 2])
    (1, 4)
    
	Include these tokens in the code: [ :(
	Do not include these tokens in the code: [:
	"""
    return (min(numbers), max(numbers))


def get_min_max_dict(numbers: List[int]) -> Tuple[int, int]:
    """ From a given list of integers, return a tuple with the minimum and maximum value found.
    >>> get_min_max_dict([1, 2, 3, 2, 3, 4, 2])
    (1, 4)
    
	Include these tokens in the code: [ :(
	Do not include these tokens in the code: [:
	"""
    return min(numbers), max(numbers)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
