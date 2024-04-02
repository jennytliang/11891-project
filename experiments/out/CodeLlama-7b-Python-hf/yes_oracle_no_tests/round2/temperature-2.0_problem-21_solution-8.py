from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    
	Include these tokens in the code: ma , mi = max ( numbers ), min (
	"""
    ma = max(numbers)
    mi = min(numbers)
    return [((n - mi) / (ma - mi)) for n in numbers]


def rescale_to_range(numbers: List[float], min_value: float = 0.0, max_value: float = 1.0) -> List[float]:
    """Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become min_value and the largest will become max_value
    >>> rescale_to_range([1.0, 2.0, 3.0, 4.0, 5.0], 0.0, 1.0)
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    ma = max(numbers)
    mi = min(numbers)
    return [((n - mi) / (ma - mi)) * (max_value - min_value) + min_value for n in numbers]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
