from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_so_far = [numbers[0]]
    for number in numbers[1:]:
        max_so_far.append(max(max_so_far[-1], number))
    return max_so_far


if __name__ == "__main__":
    import doctest

    doctest.testmod()
