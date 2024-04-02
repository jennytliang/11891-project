from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    
	Include these tokens in the code: k = 1 / ( ma - mi
	"""


    ma, mi = max(numbers), min(num for num in numbers if num != 0)
    k = 1 / (ma - mi)

    return [num * k for num in numbers]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
