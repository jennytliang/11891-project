from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    result: List[int] = [numbers[0]]
    for num in numbers[1:]:
        result.append(max(num, result[-1]))
    return result


def rolling_max_v2(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max_v2([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    result: List[int] = [numbers[0]]
    for num in numbers[1:]:
        if num >= result[-1]:
            result.append(num)
        else:
            result.append(result[-1])
    return result


def rolling_max_v3(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max_v3([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    result: List[int] = [numbers[0]]
    for num in numbers[1:]:
        if num >= result[-1]:
            result.append(num)
        else:
            result.append(result[-1])
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()

