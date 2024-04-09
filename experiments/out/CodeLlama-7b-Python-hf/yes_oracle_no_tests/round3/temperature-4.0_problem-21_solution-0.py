from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    
	Include these tokens in the code: ma , mi
	Do not include these tokens in the code: min _ num
	"""
    min_num = min(numbers)
    max_num = max(numbers)
    return [(num - min_num) / (max_num - min_num) for num in numbers]


def rescale_to_range(numbers: List[float], min_: float, max_: float) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become min_ and the largest will become max_
    >>> rescale_to_range([1.0, 2.0, 3.0, 4.0, 5.0], 0.0, 1.0)
    [0.25, 0.5, 0.75, 1.0, 1.25]
    
	Include these tokens in the code: ma , mi
	Do not include these tokens in the code: min _ num
	"""
    min_num = min(numbers)
    max_num = max(numbers)
    return [((num - min_num) / (max_num - min_num)) * (max_ - min_) + min_ for num in numbers]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
