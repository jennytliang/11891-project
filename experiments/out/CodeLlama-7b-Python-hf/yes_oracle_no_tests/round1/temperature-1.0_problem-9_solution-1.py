from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: max _ so _ far : List
	"""
    length: int = len(numbers)
    rolling_max_list: List[int] = [numbers[0]]
    for i in range(length - 1):
        current_maximum: int = max(rolling_max_list[i], numbers[i + 1])
        rolling_max_list.append(current_maximum)

    return rolling_max_list
