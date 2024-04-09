from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    
	Include these tokens in the code: k = 1
	Do not include these tokens in the code: if ma == mi : return [ 0
	"""


    ma, mi = max(numbers), min(number for number in numbers if number != 0)
    if ma == mi:
        return [0 for number in numbers]

    k = 1 / (ma - mi)
    return [k * (number - mi) for number in numbers]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
