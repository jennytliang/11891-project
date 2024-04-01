from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max_list: List[int] = []
    max_number: int = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
        rolling_max_list.append(max_number)
    return rolling_max_list


def rolling_min(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling minimum element found until given moment
    in the sequence.
    >>> rolling_min([1, 2, 3, 2, 3, 4, 2])
    [1, 1, 1, 2, 2, 2, 2]
    """
    rolling_min_list: List[int] = []
    min_number: int = numbers[0]
    for number in numbers:
        if number < min_number:
            min_number = number
        rolling_min_list.append(min_number)
    return rolling_min_list


if __name__ == "__main__":
    import doctest

    doctest.testmod()
