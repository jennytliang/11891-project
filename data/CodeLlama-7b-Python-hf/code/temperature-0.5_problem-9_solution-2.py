from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_so_far: List[int] = []
    for number in numbers:
        if not max_so_far or number >= max_so_far[-1]:
            max_so_far.append(number)
        else:
            max_so_far.append(max_so_far[-1])
    return max_so_far


if __name__ == '__main__':
    import doctest

    doctest.testmod()