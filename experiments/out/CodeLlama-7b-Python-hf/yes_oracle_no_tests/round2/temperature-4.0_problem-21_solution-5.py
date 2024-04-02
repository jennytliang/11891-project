from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    
	Include these tokens in the code: , mi
	"""

 
    min_value = min(numbers)
    max_value = max(numbers)
    new_numbers = []
    for num in numbers:
        new_numbers.append((num - min_value)/(max_value - min_value))
    return new_numbers


def main():
    assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]
    assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0, 6.0]) == [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
    assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]) == [0.0, 0.17, 0.34, 0.51, 0.68, 0.85, 1.0]
    assert rescale_to_unit([1.0, 3.0, 5.0, 7.0]) == [0.0, 0.33, 0.67, 1.0]
    assert rescale_to_unit([-2.0, -1.0, 0.0, 1.0, 2.0]) == [0.0, 0.125, 0.25, 0.375, 0.5]
    assert rescale_to_unit([-1.0, 0.0, 1.0, 2.0, 3.0]) == [0.0, 0.125, 0.375, 0.625, 0.875]
    assert rescale_to_unit([-2.0, -1.0,