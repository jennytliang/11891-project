from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    
	Include these tokens in the code: ma , mi
	Do not include these tokens in the code: result : List [ float
	"""
    result: List[float]
    lowest_value: float
    highest_value: float
    ma: float
    mi: float

    # Write your code here.
    mi = min(numbers)
    ma = max(numbers)
    if mi == ma == 0.0: return [0.0 for num in numbers]
    n_numbers: float = len(numbers)
    lowest_value = (1 / (ma - mi)) * mi
    highest_value = 1 - lowest_value
    result: List[float] = (highest_value - lowest_value) / n_numbers * [float(i) for i in range(1, len(numbers) + 1)]
#    return result

