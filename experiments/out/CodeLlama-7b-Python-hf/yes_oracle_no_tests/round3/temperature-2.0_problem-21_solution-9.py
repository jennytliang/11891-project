from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    
	Include these tokens in the code: numbers
	Do not include these tokens in the code: num for num in if num != 0
	"""



    ma, mi = max(numbers), min(numbers)
    return [((num - mi) / (ma - mi)) for num in numbers]


def rescale_to_unit_inplace(numbers: List[float]) -> None:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit_inplace([1.0, 2.0, 3.0, 4.0, 5.0])
    >>> [0.0, 0.25, 0.5, 0.75, 1.0]
    
	Include these tokens in the code: numbers
	Do not include these tokens in the code: num for num in if num != 0
	"""



    ma, mi = max(numbers), min(numbers)
    for i in range(len(numbers)):
        numbers[i] = (numbers[i] - mi) / (ma - mi)


def rescale_to_unit_inplace_2(numbers: List[float]) -> None:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit_inplace_2([1.0, 2.0, 3.0, 4.0, 5.0])
    >>> [0.0, 0.25, 0.5, 0.75, 1.0]
    
	Include these tokens in the code: numbers
	Do not include these tokens in the code: num for num in if num != 0
	"""



    ma, mi = max(numbers), min(numbers)
    for i in range(len(numbers)):
        numbers[i] = (numbers[i] - mi) * (1 / (ma - mi))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
