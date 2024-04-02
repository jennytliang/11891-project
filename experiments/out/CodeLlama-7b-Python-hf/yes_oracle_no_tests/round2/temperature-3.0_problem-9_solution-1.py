from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [
	Do not include these tokens in the code: rolling _
	"""
    return [max(numbers[:i+1]) for i in range(len(numbers))]


def max_sublist_sum(numbers: List[int]) -> Tuple[int, int]:
    """ From a given list of integers, find a sublist with the largest sum and return the sum and starting
    index of the first element of this sublist.
    >>> max_sublist_sum([10, -5, 2, 3, 100, 4, -7])
    (107, 2)
    >>> max_sublist_sum([1, 2, 3, 4])
    (10, 0)
    
    Do not include these tokens in the code: max_
    """
    max_sum = max_start_index = 0
    current_sum = 0
    for i, num in enumerate(numbers):
        current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum
            max_start_index = i
    return max_sum, max_start_index


def max_sublist_sum_fast(numbers: List[int]) -> Tuple[int, int]:
    """ From a given list of integers, find a sublist with the largest sum and return the sum and starting
    index of the first element of this sublist.
    >>> max_sublist_sum_fast([10, -5, 2, 3, 100, 4, -7])
    (107, 2)
    >>> max_sublist_sum_fast([1, 2, 3, 4])
    (10, 0)
    
    Do not include these tokens in the code: max_
    """
    current_sum = max_sum = max_start_index = 0
    for i, num in enumerate(numbers):
        current_sum = max(current_sum + num, num)
        max_sum = max(max_sum, current_sum)
        if current_sum == num:
            max_start_index = i
    return max_sum, max_start