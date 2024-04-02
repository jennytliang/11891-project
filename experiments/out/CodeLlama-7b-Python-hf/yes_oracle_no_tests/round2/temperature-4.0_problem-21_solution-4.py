from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    
	Include these tokens in the code: , mi
	"""

 
    pass


def rescale_to_unit_in_place(numbers: List[float]) -> None:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1, without creating a new list
    >>> numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
    >>> rescale_to_unit_in_place(numbers)
    >>> numbers
    [0.0, 0.25, 0.5, 0.75, 1.0]
    
	Include these tokens in the code: , mi
	"""

 
    pass


def rescale_to_unit_with_min(numbers: List[float], min_value: float) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become min_value and the largest will become 1
    >>> rescale_to_unit_with_min([1.0, 2.0, 3.0, 4.0, 5.0], 0.5)
    [0.5, 0.625, 0.75, 0.875, 1.0]
    
	Include these tokens in the code: , mi
	"""

 
    pass


def rescale_to_unit_with_min_in_place(numbers: List[float], min_value: float) -> None:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become min_value and the largest will become 1, without creating a new list
    >>> numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
    >>> rescale_to_unit_with_min_in_place(numbers, 0.5)
    >>> numbers
    [0.5, 