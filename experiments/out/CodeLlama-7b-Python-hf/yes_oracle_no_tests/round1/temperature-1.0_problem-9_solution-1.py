from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: max _ so _ far : List
	"""
    rolling_max: List[int] = []
    so_far: List[int] = []
    for number in numbers:
        if not so_far or number >= so_far[-1]:
            so_far.append(number)
        else:
            so_far = so_far[:len(so_far) - 1] + [number]
        rolling_max.append(so_far[-1])
    return rolling_max


def max_sliding_window(numbers: List[int], window_size: int) -> List[int]:
    """ From a given list of integers, generate a list of maximum element found in rolling window of a given size.
    >>> max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3)
    [3, 3, 5, 5, 6, 7]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: _ _ _ : List
	"""
    max_sliding_window: List[int] = []
    _: List[int] = []
    for number in numbers:
        if not _ or number >= _[-1]:
            _.append(number)
        else:
            _ = _[:len(_) - window_size] + [number]
        if len(_) == window_size:
            max_sliding_window.append(_[-1])
    return max_sliding_window


def max_product_three(numbers: List[int]) -> Tuple[int, int, int]:
    """ From a given list of integers, generate a tuple of three integers representing the maximum product of three
    consecutive integers in the list.
    >>> max_product_three([-10, -10, 5, 2, 4, 3, -20, 3, -4, 14, -5, -2])
    (-20, 3, 14)
    
	Include these tokens in the code: return
	Do not include these tokens in the code: _ _ _
	""