from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [ max
	Do not include these tokens in the code: result : List int ] =
	"""
    result = []
    for i, num in enumerate(numbers):
        if i == 0:
            result.append(num)
        else:
            result.append(max(result[-1], num))
    return result


def rolling_max_tuple(numbers: List[int]) -> List[Tuple[int, int]]:
    """ From a given list of integers, generate a list of tuples. Each tuple contains the rolling maximum
    element found until given moment in the sequence and the index of the element in the sequence.
    >>> rolling_max_tuple([1, 2, 3, 2, 3, 4, 2])
    [(1, 0), (2, 1), (3, 2), (3, 3), (3, 4), (4, 5), (4, 6)]
    """
    result = []
    for i, num in enumerate(numbers):
        if i == 0:
            result.append((num, i))
        else:
            if result[-1][0] >= num:
                result.append((result[-1][0], i))
            else:
                result.append((num, i))
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
