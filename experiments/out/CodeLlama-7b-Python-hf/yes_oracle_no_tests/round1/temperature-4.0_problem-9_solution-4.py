from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: size = len ( numbers )
	"""
    max_so_far: int = 0
    result: List[int] = []
    for number in numbers:
        max_so_far = max(max_so_far, number)
        result.append(max_so_far)
    return result


def max_sequence(numbers: List[int]) -> Tuple[int, int]:
    """ From a given list of integers, generate a tuple of first and last index of the longest increasing subsequence.
    >>> max_sequence([1, 101, 10, 5, 2, 3, 2, 0, 19])
    (1, 2)
    >>> max_sequence([1, 2, 3, 4, 5])
    (0, 4)
    
	Include these tokens in the code: return
	Do not include these tokens in the code: size = len ( numbers )
	"""
    max_so_far: int = 0
    max_ending_here: int = 0
    first_index: int = 0
    last_index: int = 0
    for i, number in enumerate(numbers):
        if number > max_so_far:
            max_so_far = number
            last_index = i
        if max_so_far > max_ending_here:
            max_ending_here = max_so_far
            first_index = last_index
    return first_index, last_index


def max_sequence_recursive(numbers: List[int]) -> Tuple[int, int]:
    """ From a given list of integers, generate a tuple of first and last index of the longest increasing subsequence.
    >>> max_sequence_recursive([1, 101, 10, 5, 2, 3, 2, 0, 19])
    (1, 2)
    >>> max_sequence_recursive([1, 2, 3, 4, 5])
    (0, 4)
    
	Include these tokens in the code: return
	Do not include these tokens in the code: size =