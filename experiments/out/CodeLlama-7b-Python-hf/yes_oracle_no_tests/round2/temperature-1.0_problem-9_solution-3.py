from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [ max
	Do not include these tokens in the code: _ so _ far = None
	"""
    result: List[int] = []
    _so_far = None
    for num in numbers:
        if _so_far is None or _so_far < num:
            _so_far = num
        result.append(_so_far)
    return result


def find_pair_given_sum(numbers: List[int], sum_: int) -> Tuple[int, int]:
    """  Given numbers in a list, find a pair of elements that has equal sum. """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
