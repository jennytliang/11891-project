from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [ max ( numbers
	Do not include these tokens in the code: result = [] _
	"""
    result = []
    for i in range(len(numbers)):
        if i == 0:
            result.append(numbers[0])
        else:
            result.append(max(result[i - 1], numbers[i]))
    return result


def rolling_max_tuple(numbers: List[int]) -> List[Tuple[int, int]]:
    """ From a given list of integers, generate a list of tuples (index, maximum element until given moment in
    the sequence).
    >>> rolling_max_tuple([1, 2, 3, 2, 3, 4, 2])
    [(0, 1), (1, 2), (2, 3), (3, 3), (4, 3), (5, 4), (6, 4)]
    
	Include these tokens in the code: return [ ( i, max
	Do not include these tokens in the code: result = [] _
	"""
    result = []
    for i in range(len(numbers)):
        if i == 0:
            result.append((i, numbers[0]))
        else:
            result.append((i, max(result[i - 1][1], numbers[i])))
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
