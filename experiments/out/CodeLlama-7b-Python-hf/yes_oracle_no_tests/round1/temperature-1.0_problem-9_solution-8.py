from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: max _ so _ far = numbers
	"""
    rolling_max_numbers = []
    max_val = numbers[0]
    for num in numbers:
        if num >= max_val:
            max_val = num
        rolling_max_numbers.append(max_val)
    return rolling_max_numbers


if __name__ == '__main__':
    import doctest

    doctest.testmod()

