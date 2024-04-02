from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    
	Do not include these tokens in the code: assert len ( numbers ) >=
	"""
    minimum = float(min(numbers))
    maximum = float(max(numbers))
    unit_numbers = []
    for number in numbers:
        unit_number = (number - minimum) / (maximum - minimum)
        unit_numbers.append(unit_number)
    return unit_numbers


def rescale_to_unit_inplace(numbers: List[float]) -> None:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit_inplace([1.0, 2.0, 3.0, 4.0, 5.0])
    >>> numbers
    [0.0, 0.25, 0.5, 0.75, 1.0]
    
	Do not include these tokens in the code: assert len ( numbers ) >=
	"""
    minimum = float(min(numbers))
    maximum = float(max(numbers))
    for index, number in enumerate(numbers):
        numbers[index] = (number - minimum) / (maximum - minimum)


def rescale_with_new_min_and_max(numbers: List[float], new_min: float, new_max: float) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become new_min and the largest will become new_max
    >>> rescale_with_new_min_and_max([1.0, 2.0, 3.0, 4.0, 5.0], 0.0, 1.0)
    [0.0, 0.25, 0.5, 0.75, 1.0]
    
	Do not include these tokens in the code: assert len ( numbers ) >=
	"""
    minimum = float(min(numbers))
    maximum = float(max(numbers))
    new_numbers = []
    for number in numbers:
        new