from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: max _ so _ far = numbers
	"""
    rolling_max: List[int] = []
    
    for so_far in numbers:
        max_ = max(rolling_max[-1] if rolling_max else 0, so_far)
        rolling_max.append(max_)

    return rolling_max


if __name__ == '__main__':
    import doctest
    doctest.testmod()
