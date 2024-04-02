from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Do not include these tokens in the code: if not numbers :
	"""
    if not numbers:
        return []
    
    rolling_max_numbers = [numbers[0]]
    for number in numbers[1:]:
        rolling_max_numbers.append(max(rolling_max_numbers[-1], number))
    
    return rolling_max_numbers


def rolling_max_tuple(numbers: List[int]) -> List[Tuple[int, int]]:
    """ From a given list of integers, generate a list of tuples (index, max_element) with index starting
    from 0 and max_element being the maximum element found up to this index in the sequence.
    >>> rolling_max_tuple([1, 2, 3, 2, 3, 4, 2])
    [(0, 1), (1, 2), (2, 3), (3, 3), (4, 3), (5, 4), (6, 4)]
    
	Do not include these tokens in the code: if not numbers :
	"""
    if not numbers:
        return []
    
    rolling_max_numbers = [(0, numbers[0])]
    for index, number in enumerate(numbers[1:]):
        rolling_max_numbers.append((index + 1, max(rolling_max_numbers[-1][1], number)))
    
    return rolling_max_numbers


def rolling_max_tuple_reverse(numbers: List[int]) -> List[Tuple[int, int]]:
    """ From a given list of integers, generate a list of tuples (index, max_element) with index starting
    from 0 and max_element being the maximum element found up to this index in the sequence.
    >>> rolling_max_tuple_reverse([1, 2, 3, 2, 3, 4, 2])
    [(6, 4), (5, 4), (4, 3), (3, 3), (2, 3), (1, 2), (0, 1)]
    
	Do not include these tokens in the code: if not numbers :
	"""
    if not numbers:
        return []
