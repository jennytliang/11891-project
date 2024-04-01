from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Do not include these tokens in the code: # if the list is empty
	"""
    if not numbers:
        return []
    max_number = numbers[0]
    result = [max_number]
    for num in numbers[1:]:
        if num > max_number:
            max_number = num
        result.append(max_number)
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
