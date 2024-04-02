from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Do not include these tokens in the code: if not numbers :
	"""
    result: List[int] = []
    if numbers:
        max_so_far = max(numbers)
        result = [max_so_far] * len(numbers)
        for i in range(1, len(numbers)):
            max_so_far = max(max_so_far, numbers[i])
            result[i] = max_so_far
    return result


def rolling_max_2(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Do not include these tokens in the code: if not numbers :
	"""
    result: List[int] = []
    if numbers:
        max_so_far = max(numbers)
        result = [max_so_far] * len(numbers)
        for i in range(1, len(numbers)):
            max_so_far = max(max_so_far, numbers[i])
            result[i] = max_so_far
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(rolling_max([1, 2, 3, 2, 3, 4, 2]))
