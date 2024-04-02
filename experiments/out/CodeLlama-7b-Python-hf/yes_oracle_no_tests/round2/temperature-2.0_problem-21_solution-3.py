from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    
	Include these tokens in the code: , mi
	"""

 
    return [ (max(numbers) - min(numbers)) * (i - min(numbers)) / (max(numbers) - min(numbers)) + min(numbers) for i in numbers]


def rescale_to_unit_test():
    rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    rescale_to_unit([0.0, 0.0, 0.0, 0.0, 0.0])
    rescale_to_unit([100.0, 200.0, 300.0, 400.0, 500.0])
    rescale_to_unit([0.0, 100.0, 200.0, 300.0, 400.0])
    rescale_to_unit([100.0, 200.0, 300.0, 400.0, 500.0])
    rescale_to_unit([-100.0, 0.0, 100.0, 200.0, 300.0])
    rescale_to_unit([-100.0, -200.0, -300.0, -400.0, -500.0])
