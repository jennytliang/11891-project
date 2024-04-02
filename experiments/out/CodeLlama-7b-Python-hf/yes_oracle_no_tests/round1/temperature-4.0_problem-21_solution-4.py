from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    
	Include these tokens in the code: ma , mi
	Do not include these tokens in the code: numbers
	"""
    ma = max(numbers)
    mi = min(numbers)
    return [0 if mi == ma else (n - mi) / (ma - mi) for n in numbers]


def rescale_to_range(numbers: List[float], new_min: float, new_max: float) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become new_min and the largest will become new_max
    >>> rescale_to_range([1.0, 2.0, 3.0, 4.0, 5.0], -1.0, 1.0)
    [-1.0, -0.25, 0.0, 0.25, 1.0]
    
	Include these tokens in the code: ma , mi , new_min , new_max , range_size
	Do not include these tokens in the code: numbers
	"""
    ma = max(numbers)
    mi = min(numbers)
    return [new_min + (n - mi) * (new_max - new_min) / (ma - mi) for n in numbers]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
