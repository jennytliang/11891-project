from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Do not include these tokens in the code: if not numbers :
	"""
    rolling_max_numbers = []
    rolling_max_number = 0
    for i in range(len(numbers)):
        if numbers[i] > rolling_max_number:
            rolling_max_number = numbers[i]
        rolling_max_numbers.append(rolling_max_number)
    return rolling_max_numbers


if __name__ == "__main__":
    import doctest

    doctest.testmod()
