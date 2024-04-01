from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max: List[int] = []
    current_max: int = numbers[0]
    for number in numbers:
        if number > current_max:
            current_max = number
        rolling_max.append(current_max)
    return rolling_max


if __name__ == '__main__':
    import doctest
    doctest.testmod()
