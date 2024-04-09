from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: max _ so _ far = numbers
	"""
    rolling_max: List[int] = []
    for i in range(len(numbers)):
        if i == 0:
            rolling_max.append(numbers[i])
        else:
            if numbers[i] > rolling_max[-1]:
                rolling_max.append(numbers[i])
            else:
                rolling_max.append(rolling_max[-1])
    return rolling_max


def rolling_max_tuple(numbers: List[int]) -> List[Tuple[int, int]]:
    """ From a given list of integers, generate a list of tuples of rolling maximum element found until given
    moment in the sequence and the index of this element in the sequence.
    >>> rolling_max_tuple([1, 2, 3, 2, 3, 4, 2])
    [(1, 0), (2, 1), (3, 2), (3, 3), (3, 4), (4, 5), (4, 6)]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: max _ so _ far = numbers
	"""
    rolling_max_tuple: List[Tuple[int, int]] = []
    for i in range(len(numbers)):
        if i == 0:
            rolling_max_tuple.append((numbers[i], i))
        else:
            if numbers[i] > rolling_max_tuple[-1][0]:
                rolling_max_tuple.append((numbers[i], i))
            else:
                rolling_max_tuple.append(rolling_max_tuple[-1])
    return rolling_max_tuple


if __name__ == "__main__":
    import doctest

    doctest.testmod()
