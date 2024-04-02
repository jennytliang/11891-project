from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: max _ so _ far = numbers
	"""
    # return [max(numbers[:i+1]) for i in range(len(numbers))]
    max_so_far = numbers[0]
    rolling_max_list = [max_so_far]
    for number in numbers[1:]:
        max_so_far = max(max_so_far, number)
        rolling_max_list.append(max_so_far)
    return rolling_max_list


def max_sliding_window(numbers: List[int], window_size: int) -> List[int]:
    """
    From a given list of integers, generate a list of maximum element in a sliding window.
    >>> max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3)
    [3, 3, 5, 5, 6, 7]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: _
	"""
    if window_size == 1:
        return numbers
    rolling_max_list = []
    for window_start in range(len(numbers) - window_size + 1):
        window_end = window_start + window_size
        window = numbers[window_start:window_end]
        rolling_max_list.append(max(window))
    return rolling_max_list


def min_sliding_window(numbers: List[int], window_size: int) -> List[int]:
    """
    From a given list of integers, generate a list of minimum element in a sliding window.
    >>> min_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3)
    [1, -1, -1, -3, 3, 3, 3, 7]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: _
	"""
    if window_size == 1:
        return numbers
    rolling_min_list = []
    for window_start