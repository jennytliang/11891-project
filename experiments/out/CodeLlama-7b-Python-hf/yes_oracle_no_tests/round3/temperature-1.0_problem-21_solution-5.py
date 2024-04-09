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
    return [ma / mi for ma, mi in zip([1, max_num], [min_num, 1])]


def rescale_to_range(numbers: List[float], new_min: float, new_max: float) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become new_min and the largest will become new_max
    >>> rescale_to_range([1.0, 2.0, 3.0, 4.0, 5.0], 0.0, 10.0)
    [0.0, 2.0, 4.0, 6.0, 8.0]
    
	Include these tokens in the code: new_max , new_min
	Do not include these tokens in the code: new_min , new_max
	"""
    min_num = min(numbers)
    max_num = max(numbers)
    return [new_min + (new_max - new_min) * (num - min_num) / (max_num - min_num) for num in numbers]


if __name__ == '__main__':
    import doctest

    doctest.testmod()
