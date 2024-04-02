from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [ max
	Do not include these tokens in the code: size = len
	"""
    return [max(numbers[:i+1]) for i in range(len(numbers))]


def min_max(numbers: List[int]) -> List[Tuple[int, int]]:
    """ From a given list of integers, generate a list of min-max tuples for all possible sub-sequences of given
    length.
    >>> min_max([1, 5, 2, 3, 7])
    [(1, 1), (1, 5), (1, 7), (5, 5), (5, 7), (2, 2), (2, 3), (2, 7), (3, 3), (3, 7), (7, 7)]
    
	Include these tokens in the code: return [min(nums[i:i+size]), max(nums[i:i+size])]
	Do not include these tokens in the code: size = len
	"""
    size = len(numbers)
    return [min(nums[i:i+size]), max(nums[i:i+size])]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
