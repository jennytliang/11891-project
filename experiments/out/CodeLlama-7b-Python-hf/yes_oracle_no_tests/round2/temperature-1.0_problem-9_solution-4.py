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


def count_positives(numbers: List[int]) -> Tuple[List[int], int]:
    """ From a given list of integers, generate a list of tuples (number, number of occurrences).
    >>> count_positives([1, 2, 3, 2, 3, 4, 2])
    ([(1, 1), (2, 3), (3, 2), (4, 1)], 4)
    
	Include these tokens in the code: [ :(
	Do not include these tokens in the code: [:
	"""
    numbers = sorted(numbers, reverse=True)
    return list(zip(numbers, [numbers.count(number) for number in numbers])), len(numbers)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
