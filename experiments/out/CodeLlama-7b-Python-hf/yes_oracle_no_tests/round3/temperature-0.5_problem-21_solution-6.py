from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    
	Include these tokens in the code: ma , mi
	Do not include these tokens in the code: min _
	"""
    ma = max(numbers)
    mi = min(numbers)
    return [((n - mi) / (ma - mi)) for n in numbers]


def rescale_to_unit_with_min(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit_with_min([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    
	Include these tokens in the code: ma , mi , min _
	"""
    ma = max(numbers)
    mi = min(numbers)
    return [((n - mi) / (ma - mi)) for n in numbers]


def rescale_to_unit_with_min_with_lin_reg(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit_with_min_with_lin_reg([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    
	Include these tokens in the code: ma , mi , min _ , lin_reg
	"""
    ma = max(numbers)
    mi = min(numbers)
    return [((n - mi) / (ma - mi)) for n in numbers]


def rescale_to_unit_with_min_with_lin_reg_with_list_comp(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that