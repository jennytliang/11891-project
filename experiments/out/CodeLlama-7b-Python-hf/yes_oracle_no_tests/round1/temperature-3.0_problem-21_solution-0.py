from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    
	Include these tokens in the code: ma , mi = max
	Do not include these tokens in the code: assert len
	"""
    ma = max(numbers)
    mi = min(numbers)
    return [(x - mi) / (ma - mi) for x in numbers]


def rescale_to_unit_test():
    assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]
    assert rescale_to_unit([2.0, 4.0, 6.0, 8.0, 10.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]
    assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0, 6.0]) == [0.0, 0.25, 0.5, 0.75, 1.0, 1.25]
    assert rescale_to_unit([1.0, 1.0, 1.0, 1.0, 1.0, 1.0]) == [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]) == [0.0, 0.125, 0.25, 0.375, 0.5, 0.625, 0.75]


if __name__ == '__main__':
    rescale_to_unit_test()
