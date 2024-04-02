from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    
	Include these tokens in the code: ma , mi = max ( numbers ), min (
	"""
    ma = max(numbers)
    mi = min(numbers)
    return [num/mi for num in numbers]


def mean(numbers: List[int]) -> float:
    """
    >>> mean([1.0, 2.0, 3.0, 4.0, 5.0])
    3.0
    >>> mean([1.0, 2.0, 3.0, 4.0, 5.0,])
    3.0
    >>> mean([1.0, 1.0, 2.0, 3.0, 5.0,])
    2.25
    >>> mean([1.0, -2.0, 3.0, 4.0, 5.0,])
    0.25
    >>> mean([10.0, 2.0, -4.0, 4.0, 5.0,])
    2.375
    """ 
    return sum(numbers) / len(numbers)

def median(numbers: List[int]) -> float:
    """
    >>> median([1.0, 2.0, 3.0, 4.0, 5.0])
    3.0
    >>> median([1.0, 1.0, 1.0, 1.0, 1.0,])
    1.0
    >>> median([10.0, 2.0, -4.0, 4.0, 5.0,])
    3.0
    >>> median([10.0, 2.0, 2.0, 4.0, 5.0,])
    3.0
    """
    sorted_numbers = sorted(numbers)
    if len(numbers) % 2 == 0:
        i = len(sorted_numbers) // 2
        return sum(sorted_numbers[i - 1: i + 1]) / 2.0
    else:
        i = len(sorted_numbers) // 2 
        return sorted_numbers[i]


if __name__ == "__main