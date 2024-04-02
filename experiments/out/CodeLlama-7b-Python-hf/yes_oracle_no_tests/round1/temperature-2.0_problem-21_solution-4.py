from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    
	Include these tokens in the code: ma , mi = max
	Do not include these tokens in the code: if len
	"""
    ma = max(numbers)
    mi = min(numbers)
    return [((n-mi)/(ma-mi)) for n in numbers]


def rescale_to_unit_with_clip(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1, but clip any values
    outside of [0, 1] to be within that range
    >>> rescale_to_unit_with_clip([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    
	Include these tokens in the code: ma , mi = max, min, clip
	Do not include these tokens in the code: if len
	"""
    ma = max(numbers)
    mi = min(numbers)
    return [min(max(((n-mi)/(ma-mi)), 0), 1) for n in numbers]


def rescale_to_unit_with_shift(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1, and shift the whole
    list by 0.5
    >>> rescale_to_unit_with_shift([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.5, 0.75, 1.0, 1.25, 1.5]
    
	Include these tokens in the code: ma , mi = max, min, shift
	Do not include these tokens in the code: if len
	"""
    ma = max(numbers)
    mi = min(numbers)
    return [(n-mi)/(ma-mi) + 0.5 for n in numbers]


if __