from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [ max ( numbers [ :( i + 1
	Do not include these tokens in the code: _ window = []
	"""
    if len(numbers) == 0:
        return []
    window: List[int] = [max(numbers)]

    for i in range(1, len(numbers)):
        if numbers[i] > window[i - 1]:
            window.append(numbers[i])
        else:
            window.append(window[i - 1])
    return window


def rolling_min(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling minimum element found until given moment
    in the sequence.
    >>> rolling_min([1, 2, 3, 2, 3, 4, 2])
    [1, 1, 1, 2, 2, 2, 2]
    
	Include these tokens in the code: return [ min ( numbers [ :( i + 1
	Do not include these tokens in the code: _ window = []
	"""
    if len(numbers) == 0:
        return []
    window: List[int] = [min(numbers)]

    for i in range(1, len(numbers)):
        if numbers[i] < window[i - 1]:
            window.append(numbers[i])
        else:
            window.append(window[i - 1])
    return window


def running_median(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling median element found until given moment
    in the sequence.
    >>> running_median([1, 2, 3, 2, 3, 4, 2])
    [1, 1.5, 2, 2.5, 3, 3, 3]
    
	Include these tokens in the code: return [ median ( numbers [ :( i + 1
	Do not include these tokens in the code: _ window = []
	"""
    if len(numbers) == 0:
        return []
    window: List[int] = [numbers[0]]

    for i in range(1, len(numbers)):