from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []

    max_so_far: List[int] = [numbers[0]]
    for number in numbers[1:]:
        max_so_far.append(max(number, max_so_far[-1]))

    return max_so_far


def rolling_min(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling minimum element found until given moment
    in the sequence.
    >>> rolling_min([1, 2, 3, 2, 3, 4, 2])
    [1, 1, 1, 2, 2, 2, 2]
    """
    if not numbers:
        return []

    min_so_far: List[int] = [numbers[0]]
    for number in numbers[1:]:
        min_so_far.append(min(number, min_so_far[-1]))

    return min_so_far


if __name__ == "__main__":
    import doctest
    doctest.testmod()
