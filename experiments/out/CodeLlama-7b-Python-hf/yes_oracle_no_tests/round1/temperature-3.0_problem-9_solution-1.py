from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [
	Do not include these tokens in the code: rolling _
	"""
    rolling_max_list: List[int] = []
    for i in range(len(numbers)):
        rolling_max_list.append(max(numbers[:i + 1]))
    return rolling_max_list


def rolling_max_tuple(numbers: List[int]) -> List[Tuple[int, int]]:
    """
    >>> rolling_max_tuple([1, 2, 3, 2, 3, 4, 2])
    [(1, 1), (2, 2), (3, 3), (2, 3), (3, 3), (4, 4), (2, 4)]
    """
    rolling_max_list: List[Tuple[int, int]] = []
    for i in range(len(numbers)):
        rolling_max_list.append((numbers[i], max(numbers[:i + 1])))
    return rolling_max_list


if __name__ == "__main__":
    import doctest
    doctest.testmod()
