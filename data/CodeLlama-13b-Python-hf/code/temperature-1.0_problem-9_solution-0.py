from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_so_far = numbers[0]
    result = [max_so_far]
    for i in range(1, len(numbers)):
        max_so_far = max(max_so_far, numbers[i])
        result.append(max_so_far)
    return result


def rolling_min(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling minimum element found until given moment
    in the sequence.
    >>> rolling_min([1, 2, 3, 2, 3, 4, 2])
    [1, 1, 1, 2, 2, 2, 2]
    """
    min_so_far = numbers[0]
    result = [min_so_far]
    for i in range(1, len(numbers)):
        min_so_far = min(min_so_far, numbers[i])
        result.append(min_so_far)
    return result