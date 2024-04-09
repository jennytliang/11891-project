from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [
	Do not include these tokens in the code: result : List int ] =
	"""
    result: List[int] = []
    rolling_max_value = 0

    for index, number in enumerate(numbers):
        if number > rolling_max_value:
            rolling_max_value = number

        result.append(rolling_max_value)

    return result


def rolling_max_tuple(numbers: List[int]) -> List[Tuple[int, int]]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max_tuple([1, 2, 3, 2, 3, 4, 2])
    [(1, 1), (2, 2), (3, 3), (3, 3), (3, 3), (4, 4), (4, 4)]
    
	Include these tokens in the code: return [
	Do not include these tokens in the code: result : List Tuple[int, int]] =
	"""
    result: List[Tuple[int, int]] = []
    rolling_max_value = 0

    for index, number in enumerate(numbers):
        if number > rolling_max_value:
            rolling_max_value = number

        result.append((number, rolling_max_value))

    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
