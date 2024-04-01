from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max_list: List[int] = []
    current_max: int = numbers[0]

    for number in numbers:
        if number >= current_max:
            current_max = number
        rolling_max_list.append(current_max)

    return rolling_max_list


def rolling_min(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling minimum element found until given moment
    in the sequence.
    >>> rolling_min([1, 2, 3, 2, 3, 4, 2])
    [1, 1, 1, 2, 2, 2, 2]
    """
    rolling_min_list: List[int] = []
    current_min: int = numbers[0]

    for number in numbers:
        if number <= current_min:
            current_min = number
        rolling_min_list.append(current_min)

    return rolling_min_list


if __name__ == "__main__":
    import doctest

    doctest.testmod()
