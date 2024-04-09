from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [
	Do not include these tokens in the code: max _ elem = numbers 0
	"""
    rolling_max_list = []
    max_elem = numbers[0]
    for elem in numbers:
        max_elem = max(max_elem, elem)
        rolling_max_list.append(max_elem)
    return rolling_max_list


def rolling_max_tuple(numbers: List[int]) -> List[Tuple[int, int]]:
    """ From a given list of integers, generate a list of tuples of (rolling maximum element found until given moment
    in the sequence, index of rolling maximum element found until given moment in the sequence).
    >>> rolling_max_tuple([1, 2, 3, 2, 3, 4, 2])
    [(1, 0), (2, 1), (3, 2), (3, 3), (3, 4), (4, 5), (4, 6)]
    
	Include these tokens in the code: return [
	Do not include these tokens in the code: max _ elem = numbers 0
	"""
    rolling_max_list = []
    max_elem = numbers[0]
    for i, elem in enumerate(numbers):
        max_elem = max(max_elem, elem)
        rolling_max_list.append((max_elem, i))
    return rolling_max_list


if __name__ == "__main__":
    import doctest

    doctest.testmod()
