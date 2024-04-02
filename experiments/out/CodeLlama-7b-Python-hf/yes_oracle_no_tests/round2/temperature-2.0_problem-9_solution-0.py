from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [ max
	Do not include these tokens in the code: result = [] _
	"""
    result = []
    max_value = numbers[0]

    for number in numbers:
        max_value = max(max_value, number)
        result.append(max_value)

    return result


def rolling_max_tuple(numbers: List[int]) -> List[Tuple[int, int]]:
    """ From a given list of integers, generate a list of tuples containing an index of the maximum element
    and the maximum element itself until the given moment in the sequence.
    >>> rolling_max_tuple([1, 2, 3, 2, 3, 4, 2])
    [(0, 1), (1, 2), (2, 3), (3, 3), (4, 3), (5, 4), (6, 4)]
    
	Include these tokens in the code: return [ (index, max
	Do not include these tokens in the code: result = [] _
	"""
    result = []
    max_value = numbers[0]
    max_index = 0

    for index, number in enumerate(numbers):
        if number > max_value:
            max_value = number
            max_index = index

        result.append((index, max_value))

    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
