from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [
	Do not include these tokens in the code: max _ list = []
	"""
    max_list = []
    max_so_far = numbers[0]
    for item in numbers:
        max_so_far = max(max_so_far, item)
        max_list.append(max_so_far)
    return max_list


def rolling_max_tuple(numbers: List[int]) -> List[Tuple[int, int]]:
    """ From a given list of integers, generate a list of tuples (index, maximum element found until given
    moment in the sequence).
    >>> rolling_max_tuple([1, 2, 3, 2, 3, 4, 2])
    [(0, 1), (1, 2), (2, 3), (3, 3), (4, 3), (5, 4), (6, 4)]
    
	Include these tokens in the code: return [
	Do not include these tokens in the code: max_index max_so_far = 0
	"""
    max_list = []
    max_so_far = numbers[0]
    max_index = 0
    for index, item in enumerate(numbers):
        max_so_far = max(max_so_far, item)
        max_index = index if item == max_so_far else max_index
        max_list.append((max_index, max_so_far))
    return max_list


if __name__ == "__main__":
    import doctest

    doctest.testmod()
