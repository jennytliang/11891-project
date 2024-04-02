from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [
	Do not include these tokens in the code: rolling _
	"""
    return [max(numbers[:i]) for i in range(1, len(numbers) + 1)]


def max_sublist_sum(numbers: List[int]) -> int:
    """ From a given list of integers, find the maximum sum of a contiguous sublist.
    >>> max_sublist_sum([1, 2, -4, 5, -10, 7, -3, -6, -1])
    14
    """
    max_sum = 0
    curr_sum = 0
    for n in numbers:
        curr_sum = max(0, curr_sum + n)
        max_sum = max(max_sum, curr_sum)
    return max_sum


def max_sublist_sum_rec(numbers: List[int]) -> int:
    """ From a given list of integers, find the maximum sum of a contiguous sublist.
    >>> max_sublist_sum_rec([1, 2, -4, 5, -10, 7, -3, -6, -1])
    14
    """
    if len(numbers) == 1:
        return numbers[0]
    return max(
        max_sublist_sum_rec(numbers[1:]),
        max_sublist_sum_rec(numbers[:-1]),
        numbers[-1] + max_sublist_sum_rec(numbers[:-2]),
    )


def max_sublist_sum_rec2(numbers: List[int]) -> int:
    """ From a given list of integers, find the maximum sum of a contiguous sublist.
    >>> max_sublist_sum_rec2([1, 2, -4, 5, -10, 7, -3, -6, -1])
    14
    """
    return max(
        max_sublist_sum_rec2(numbers[1:]),
        max_sublist_sum_rec2(numbers[:-1]),
        numbers[-1] + numbers[-2],
    )


def max_sublist_sum_rec3(numbers