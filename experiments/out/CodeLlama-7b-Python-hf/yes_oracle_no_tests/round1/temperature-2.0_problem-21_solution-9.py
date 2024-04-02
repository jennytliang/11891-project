from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    
	Include these tokens in the code: ma , mi = max
	Do not include these tokens in the code: if len
	"""

    ma, mi = max(numbers), min(numbers)

    return list(map(lambda x: (x - mi) / (ma - mi), numbers))


def rescale_to_unit_wrapper(numbers: List[float]) -> List[float]:
    """ A wrapper function for rescale_to_unit
    """
    return rescale_to_unit(numbers)
