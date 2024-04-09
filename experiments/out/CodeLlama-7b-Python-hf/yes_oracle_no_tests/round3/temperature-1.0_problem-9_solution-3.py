from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Do not include these tokens in the code: if len ( numbers ) ==
	"""
    if not numbers:
        return []
    rolling_max_values = []
    rolling_max_values.append(numbers[0])
    for i in range(1, len(numbers)):
        rolling_max_values.append(max(rolling_max_values[i - 1], numbers[i]))
    return rolling_max_values


def max_sequence(numbers: List[int]) -> Tuple[int, int]:
    """Given a list of integers, return the start and end of the contiguous sublist with the largest sum.
    If there are more than one sublist with the same largest sum, return the sublist with the smallest starting index.
    If there are more than one sublist with the same largest sum and same smallest starting index, then return the sublist with the smallest ending index.
    If there are more than one sublist with the same largest sum, same smallest starting index and same smallest ending index, return any one of them.
    >>> max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    (2, 6)
    >>> max_sequence([])
    (None, None)
    >>> max_sequence([-2, 1, -3, 5, -1, 2, 1, -5, 4])
    (2, 4)
    >>> max_sequence([-2, -5, -1])
    (1, 2)
    >>> max_sequence([-2, -5, -1, -1])
    (3, 4)
    """
    if len(numbers) == 0:
        return None, None
    max_sum = 0
    max_start = 0
    max_end = 0
    for i in range(len(numbers)):
        cur_sum = 0
        for j in range(i, len(numbers)):
            cur_sum += numbers[j]
            if cur_sum > max_sum:
                max_sum = cur_sum
                max_start = i
                max_end = j
    return max_start, max_end
