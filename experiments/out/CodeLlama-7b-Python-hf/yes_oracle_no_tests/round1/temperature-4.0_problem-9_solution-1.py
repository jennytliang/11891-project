from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: size = len ( numbers )
	"""
    max_val = numbers[0]
    rolling_list = [numbers[0]]
    for i in range(1, len(numbers)):
        if numbers[i] >= max_val:
            max_val = numbers[i]
            rolling_list.append(max_val)
        else:
            rolling_list.append(max_val)
    return rolling_list


def max_sliding_window(seq: List[int], size: int) -> List[int]:
    """ From a given list of integers, generate a list of maximum elements found in a sliding window of given
    size.
    >>> max_sliding_window([1, 2, 3, 2, 3, 4, 2], 3)
    [3, 3, 4, 4]
    
	Include these tokens in the code: max
	Do not include these tokens in the code: max_val
	"""
    max_val = seq[0:size]
    rolling_list = []
    for i in range(size, len(seq)):
        if max(seq[i - size:i]) >= max(max_val):
            max_val = seq[i - size:i]
            rolling_list.append(max(max_val))
        else:
            rolling_list.append(max(max_val))
    return rolling_list


def max_sliding_window_optimized(seq: List[int], size: int) -> List[int]:
    """ From a given list of integers, generate a list of maximum elements found in a sliding window of given
    size.
    >>> max_sliding_window_optimized([1, 2, 3, 2, 3, 4, 2], 3)
    [3, 3, 4, 4]
    
	Include these tokens in the code: max
	Do not include these tokens in the code: max_val
	"""
    max_val = seq[0:size]
    rolling_list = []
    for i in range(size, len(seq)):
        max_val = max