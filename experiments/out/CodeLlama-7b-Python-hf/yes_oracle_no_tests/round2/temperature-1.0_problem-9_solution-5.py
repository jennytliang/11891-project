from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: max _ so _ far = numbers
	"""
    max_so_far = numbers[0]
    rolling_max_nums = [numbers[0]]
    for number in numbers[1:]:
        max_so_far = max(max_so_far, number)
        rolling_max_nums.append(max_so_far)
    return rolling_max_nums


def rolling_window_max(numbers: List[int], window_size: int) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found in
    the given window.
    >>> rolling_window_max([1, 2, 3, 2, 3, 4, 2], 3)
    [1, 2, 2, 3, 3, 3, 4]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: max _ so _ far = numbers
	"""
    max_so_far = numbers[0]
    rolling_max_nums = [numbers[0]]
    for i in range(1, len(numbers)):
        if i < window_size:
            max_so_far = max(max_so_far, numbers[i])
        else:
            max_so_far = max(max_so_far, numbers[i])
        rolling_max_nums.append(max_so_far)
    return rolling_max_nums


def find_max_crossing_subarray(
    numbers: List[int], low: int, mid: int, high: int
) -> Tuple[int, int, int]:
    """ From a given list of integers, find the maximum subarray crossing the given midpoint.
    >>> find_max_crossing_subarray([13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7], 0, 7, 15)
    (15, 9, 23)
    
