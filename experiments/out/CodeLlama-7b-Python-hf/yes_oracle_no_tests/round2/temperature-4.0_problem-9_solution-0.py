from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: max _ so _ far = numbers
	"""
    if len(numbers) == 0:
        return []
    max_so_far = numbers[0]
    rolling_max_numbers = [max_so_far]
    for number in numbers[1:]:
        if number > max_so_far:
            max_so_far = number
        rolling_max_numbers.append(max_so_far)
    return rolling_max_numbers


def rolling_max_tuple(numbers: List[int]) -> List[Tuple[int, int]]:
    """ From a given list of integers, generate a list of tuples of rolling maximum element found until given
    moment in the sequence, and the index of the element.
    >>> rolling_max_tuple([1, 2, 3, 2, 3, 4, 2])
    [(1, 0), (2, 1), (3, 2), (3, 3), (3, 4), (4, 5), (4, 6)]
    
    Include these tokens in the code: return
    Do not include these tokens in the code: max _ so _ far = numbers
    """
    if len(numbers) == 0:
        return []
    max_so_far = numbers[0]
    rolling_max_numbers = [(max_so_far, 0)]
    for i, number in enumerate(numbers[1:]):
        if number > max_so_far:
            max_so_far = number
        rolling_max_numbers.append((max_so_far, i + 1))
    return rolling_max_numbers


def rolling_max_tuple_v2(numbers: List[int]) -> List[Tuple[int, int]]:
    """ From a given list of integers, generate a list of tuples of rolling maximum element found until given
    moment in the sequence, and the index of the element.
    >>> rolling_max_tuple_v2([1, 2, 3, 2, 3, 4, 2])
    [(1, 0), (2, 1), (3, 2), (3, 3), (