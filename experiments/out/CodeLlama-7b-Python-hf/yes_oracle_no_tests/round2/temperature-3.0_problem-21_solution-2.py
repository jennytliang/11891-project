from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    
	Do not include these tokens in the code: assert len ( numbers ) >=
	"""

    # 1. Find the minimum and maximum values in the list
    max_value = max(numbers)
    min_value = min(numbers)

    # 2. Calculate the difference between the max and min values
    diff = max_value - min_value

    # 3. Divide each value by the difference, then subtract the min value
    rescaled_list = [((v - min_value) / diff) for v in numbers]

    return rescaled_list


def rescale_to_unit_test():
    assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]
    assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0, 6.0]) == [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
    assert rescale_to_unit([1.0]) == [0.0]
    assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]) == [0.0, 0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875]


if __name__ == "__main__":
    rescale_to_unit_test()
