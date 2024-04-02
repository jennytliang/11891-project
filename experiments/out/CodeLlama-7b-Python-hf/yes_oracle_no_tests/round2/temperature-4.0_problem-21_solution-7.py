from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    
	Include these tokens in the code: k = 1
	Do not include these tokens in the code: return [ (( n - mi )
	"""

    ma, mi = max(numbers), min(numbers)
    if ma == mi:
        return [0.0] * len(numbers)
    return [((n - mi) / (ma - mi)) for n in numbers]


def rescale_to_range(numbers: List[float], target_range: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become target_range[0] and the largest will become target_range[1]
    >>> rescale_to_range([1.0, 2.0, 3.0, 4.0, 5.0], [10, 20])
    [10.0, 14.0, 18.0, 22.0, 26.0]
    
	Include these tokens in the code: k = 1
	Do not include these tokens in the code: return [ (( n - mi )
	"""

    ma, mi = max(numbers), min(numbers)
    if mi == ma:
        return [target_range[0]] * len(numbers)
    return [((n - mi) * (target_range[1] - target_range[0]) / (ma - mi)) + target_range[0] for n in numbers]


def rescale_to_range_with_outliers(numbers: List[float], target_range: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become target_range[0] and the largest will become target_range[1]
    >>> rescale_to_range_with_outliers([1.0, 2.0, 3.0, 4.0, 5.0], [10, 20])
    [10.0, 14.0, 18.0, 22.0, 26.0]
    
	Include these tokens in the code: k = 1
	Do not include these tokens in the code