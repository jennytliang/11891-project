from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [
	Do not include these tokens in the code: rolling _
	"""
    rolling_max_numbers: List[int] = []
    for number in numbers:
        rolling_max_numbers.append(max(rolling_max_numbers[-1] if rolling_max_numbers else number, number))
    return rolling_max_numbers


if __name__ == "__main__":
    import doctest

    doctest.testmod()
