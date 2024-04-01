from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Do not include these tokens in the code:  max _ so _ far = [ numbers [
	"""

    rolling_max_numbers: List[int] = []

    for number in numbers:
        rolling_max_numbers.append(max(number, rolling_max_numbers[-1] if rolling_max_numbers else number))

    return rolling_max_numbers


def max_subarray_sum(numbers: List[int]) -> Tuple[int, int, int]:
    """ From a given list of integers, find a contiguous subarray with the largest sum and return the sum,
    starting index and ending index (inclusive).
    >>> max_subarray_sum([-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7])
    (-5, 9, 10)
    >>> max_subarray_sum([3, 4, 5, 6, 3, 4, 5, 6, 3, 4, 5, 6, 3, 4, 5, 6, 3, 4, 5, 6])
    (24, 0, 19)
    >>> max_subarray_sum([-1, -2, -3, -4, -5])
    (-1, 0, 0)
    
	Do not include these tokens in the code:  max _ so _ far = [ numbers [
	"""

    max_sum_numbers: List[int] = []
    max_sum_numbers.append(0)

    for number in numbers:
        max_sum_numbers.append(max(max_sum_numbers[-1] + number, number))

    max_sum = max(max_sum_numbers)
    max_sum_numbers_indexes = [i for i, v in enumerate(max_sum_numbers) if v == max_sum]
    start_index = max_sum_numbers_indexes[0]
    end_index = max_sum_numbers_indexes[-1]

    return max_sum, start_index, end_index


