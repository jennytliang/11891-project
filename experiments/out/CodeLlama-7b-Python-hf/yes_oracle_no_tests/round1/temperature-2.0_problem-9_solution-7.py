from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Do not include these tokens in the code: if not numbers :
	"""
    rolling_max_so_far = [max(numbers[0], numbers[1])]
    for index, number in enumerate(numbers[2:]):
        rolling_max_so_far.append(max(rolling_max_so_far[index], number))
    rolling_max_so_far.insert(0, max(numbers[0], numbers[1]))
    return rolling_max_so_far


def rolling_max_and_min(numbers: List[int]) -> Tuple[List[int], List[int]]:
    """ From a given list of integers, generate a tuple of lists of rolling maximum and minimum element found
    until given moment in the sequence.
    >>> rolling_max_and_min([1, 2, 3, 2, 3, 4, 2])
    ([1, 2, 3, 3, 3, 4, 4], [1, 1, 1, 2, 2, 3, 2])
    
	Do not include these tokens in the code: if not numbers :
	"""
    rolling_max_so_far = [max(numbers[0], numbers[1])]
    rolling_min_so_far = [min(numbers[0], numbers[1])]
    for index, number in enumerate(numbers[2:]):
        rolling_min_so_far.append(min(rolling_min_so_far[index], number))
        rolling_max_so_far.append(max(rolling_max_so_far[index], number))
    rolling_min_so_far.insert(0, min(numbers[0], numbers[1]))
    rolling_max_so_far.insert(0, max(numbers[0], numbers[1]))
    return rolling_max_so_far, rolling_min_so_far


if __name__ == "__main__":
    import doctest

    doctest.testmod()
