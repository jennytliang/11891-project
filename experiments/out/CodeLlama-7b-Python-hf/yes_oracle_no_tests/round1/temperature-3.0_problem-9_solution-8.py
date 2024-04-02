from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [
	Do not include these tokens in the code: rolling _
	"""
    rolling_maximum = [numbers[0]]
    for number in numbers[1:]:
        rolling_maximum.append(max(number, rolling_maximum[-1]))
    return rolling_maximum


def max_sublist_sum(numbers: List[int]) -> int:
    """ From a given list of integers, find a maximum sum of a sublist of consecutive numbers.
    >>> max_sublist_sum([1, -2, 3, 100, -9, 5, -3, 3, 2, 2, 2, 3, 4, -100])
    103
    
	Include these tokens in the code: return max(
	Do not include these tokens in the code: max _
	"""
    return max(rolling_max(numbers))


def max_sublist_sum_optimized(numbers: List[int]) -> int:
    """ From a given list of integers, find a maximum sum of a sublist of consecutive numbers.
    >>> max_sublist_sum_optimized([1, -2, 3, 100, -9, 5, -3, 3, 2, 2, 2, 3, 4, -100])
    103
    
	Include these tokens in the code: return max(
	Do not include these tokens in the code: max _
	"""
    rolling_maximum = 0
    current_maximum = 0
    for number in numbers:
        current_maximum = max(0, current_maximum + number)
        rolling_maximum = max(rolling_maximum, current_maximum)
    return rolling_maximum


def get_longest_increasing_subsequence(numbers: List[int]) -> Tuple[List[int], int]:
    """ From a given list of integers, find a longest increasing subsequence.
    >>> get_longest_increasing_subsequence([3, 5, 2, 7, 9, 4, 6, 8, 1, 10])
    ([3, 