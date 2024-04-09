from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    
	Include these tokens in the code: ma , mi
	Do not include these tokens in the code: min _ value
	"""
    smallest = min(numbers)
    largest = max(numbers)
    return [((n - smallest) / (largest - smallest)) for n in numbers]


def rescale_to_unit_test():
    assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]
    assert rescale_to_unit([10.0, 20.0, 30.0, 40.0, 50.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]
    assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0, 6.0]) == [0.0, 0.16666666666666666, 0.3333333333333333, 0.5, 0.6666666666666666, 1.0]
    assert rescale_to_unit([10.0, 20.0, 30.0, 40.0, 50.0, 60.0]) == [0.0, 0.16666666666666666, 0.3333333333333333, 0.5, 0.6666666666666666, 1.0]
    assert rescale_to_unit([10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0]) == [0.0, 0