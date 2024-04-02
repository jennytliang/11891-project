from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [
	Do not include these tokens in the code: rolling _
	"""
    if not numbers:
        return []
    rolling_max_numbers = [numbers[0]]
    for i in range(1, len(numbers)):
        rolling_max_numbers.append(max(rolling_max_numbers[i-1], numbers[i]))
    return rolling_max_numbers


def rolling_max_v2(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [
	Do not include these tokens in the code: rolling _
	"""
    if not numbers:
        return []
    rolling_max_numbers = [numbers[0]]
    for i in range(1, len(numbers)):
        if numbers[i] > rolling_max_numbers[i-1]:
            rolling_max_numbers.append(numbers[i])
        else:
            rolling_max_numbers.append(rolling_max_numbers[i-1])
    return rolling_max_numbers


def find_max_crossing_subarray(
    a: List[int], low: int, mid: int, high: int
) -> Tuple[int, int, int]:
    """ Find maximum subarray in a list of integers.
    >>> find_max_crossing_subarray([13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7], 0, 7, 14)
    (15, 7, 11)
    >>> find_max_crossing_subarray([13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 1