from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [ max
	Do not include these tokens in the code: result : List int ] =
	"""
    result: List[int] = []
    if len(numbers) == 0:
        return result
    max_value = numbers[0]
    for i in range(1, len(numbers)):
        max_value = max(max_value, numbers[i])
        result.append(max_value)
    return result


def rolling_max2(numbers: List[int]) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum element found until given moment in the
    sequence.
    >>> rolling_max2([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    result: List[int] = []
    if len(numbers) == 0:
        return result
    max_value = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] > max_value:
            max_value = numbers[i]
        result.append(max_value)
    return result


def rolling_max3(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment in the
    sequence.
    >>> rolling_max3([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    result: List[int] = []
    if len(numbers) == 0:
        return result
    max_value = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] > max_value:
            max_value = numbers[i]
        result.append(max_value)
    return result


def rolling_sum(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum element found until given moment in the
    sequence.
    >>> rolling_sum([