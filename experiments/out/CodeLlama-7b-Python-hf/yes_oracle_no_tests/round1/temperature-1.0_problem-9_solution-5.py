from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: max _ so _ far =
	"""
    max_so_far = numbers[0]
    result = [max_so_far]
    for number in numbers[1:]:
        max_so_far = max(number, max_so_far)
        result.append(max_so_far)

    return result


def max_sliding_window(numbers: List[int], window_size: int) -> List[int]:
    """ From a given list of integers, generate a list of max elements of every rolling window with given size.
    >>> max_sliding_window([1, 2, 3, 2, 3, 4, 2], 3)
    [2, 3, 3, 4, 4, 4, 4]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: _ for _ in _:
	"""
    result = []
    for i in range(len(numbers) - window_size + 1):
        result.append(max(numbers[i : i + window_size]))
    return result


def max_crossing_subarray(numbers: List[int], low: int, mid: int, high: int) -> Tuple[int, int, int]:
    """ From a given list of integers, find the maximum sum of a subarray spanning the middle index.
    >>> max_crossing_subarray([-1, 3, -5, 2, -1, 4, 4, -2], 0, 3, 7)
    (5, 4, 7)
    
	Include these tokens in the code: return
	Do not include these tokens in the code: _ for _ in _:
	"""
    left_sum = -float("inf")
    current_sum = 0
    max_left = 0
    max_right = 0

    for i in range(mid, low - 1, -1):
        current_sum += numbers[i]
        if current_sum > left_sum:
            left_sum = current_sum
            max_left = i

    right