from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    
	Include these tokens in the code: ma , mi = max ( numbers ), min (
	"""
    if len(numbers) < 2:
        raise ValueError("The list must contain at least two elements")
    ma, mi = max(numbers), min(numbers)
    if ma == mi:
        raise ValueError("All numbers are equal")
    return [(x - mi) / (ma - mi) for x in numbers]


def rescale_to_unit_in_place(numbers: List[float]) -> None:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
    >>> rescale_to_unit_in_place(numbers)
    >>> numbers
    [0.0, 0.25, 0.5, 0.75, 1.0]
    
	Include these tokens in the code: numbers[0], numbers[len(numbers) - 1] = mi, ma = min (
	"""
    if len(numbers) < 2:
        raise ValueError("The list must contain at least two elements")
    ma, mi = max(numbers), min(numbers)
    if ma == mi:
        raise ValueError("All numbers are equal")
    numbers[0], numbers[-1] = mi, ma
    for i in range(1, len(numbers) - 1):
        numbers[i] = (numbers[i] - mi) / (ma - mi)


def rescale_to_unit_in_place_with_temp(numbers: List[float]) -> None:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
    >>> rescale_to_unit_in_place_with_temp(numbers)
    >>> numbers
    [0.0, 0