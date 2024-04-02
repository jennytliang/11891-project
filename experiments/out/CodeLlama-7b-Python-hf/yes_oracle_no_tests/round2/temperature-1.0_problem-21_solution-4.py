from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    
	Do not include these tokens in the code: min _ number = numbers [ 0
	"""
    min_number = numbers[0]
    for _ in range(len(numbers) - 1):
        min_number = min(numbers[_], min_number)
    for _ in range(len(numbers) - 1):
        numbers[_] = numbers[_] - min_number / 100
    return numbers


def is_non_decreasing(numbers: List[float]) -> bool:
    """ Given list of numbers, checks if the sequence is non-decreasing
    >>> is_non_decreasing([1.0, 2.0, 3.0, 4.0, 5.0])
    True
    """
    for _ in range(len(numbers) - 1):
        if numbers[_] > numbers[_ + 1]:
            return False
    return True


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
	Do not include these tokens in the code: min _ number = numbers [ 0
    
    Example:
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]

    >>> rescale_to_unit([1.2, 3.2, 2.2, 0.2])
    [0.0, 1.0, 0.5, 0.0]
    
    Bonus: Also return a boolean which indicates if the function is non-decreasing beforehand !
    
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    (True, [0.0, 0.25, 0.5, 0.75, 1.0])
    """
    min_number =