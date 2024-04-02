from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    
	Include these tokens in the code: ma , mi
	Do not include these tokens in the code: min _ number
	"""
    mi = min(numbers)
    ma = max(numbers)

    return list(map(lambda x: (x - mi) / (ma - mi), numbers))


def rescale_to_unit_inplace(numbers: List[float]) -> None:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    >>> numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
    >>> rescale_to_unit_inplace(numbers)
    >>> numbers
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    mi = min(numbers)
    ma = max(numbers)

    for i in range(len(numbers)):
        numbers[i] = (numbers[i] - mi) / (ma - mi)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
