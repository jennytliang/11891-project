from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [
	Do not include these tokens in the code: rolling _
	"""

    if len(numbers) == 0:
        return [0]

    max_so_far = numbers[0]
    rolling_max_numbers = [0] * len(numbers)
    rolling_max_numbers[0] = max_so_far

    for i in range(1, len(numbers)):
        max_so_far = max(numbers[i], max_so_far)
        rolling_max_numbers[i] = max_so_far

    return rolling_max_numbers

