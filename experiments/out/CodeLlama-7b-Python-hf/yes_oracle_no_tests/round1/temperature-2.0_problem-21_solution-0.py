from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    
	Include these tokens in the code: ma , mi = max
	Do not include these tokens in the code: if len
	"""
    assert len(numbers) >= 2

    max_number = max(numbers)
    min_number = min(numbers)

    # Write your code here
    return [((number - min_number) / (max_number - min_number)) for number in numbers]


def main():
    print("Example:")
    print(list(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])))

    assert list(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])) == [0.0, 0.25, 0.5, 0.75, 1.0]
    assert list(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])) == [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
    assert list(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0])) == [0.0, 0.17, 0.34, 0.51, 0.68, 0.85, 1.0]
    assert list(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0])) == [0.0, 0.14, 0.28, 0.42, 0.57, 0.71, 0.85, 1.0]
    assert list(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0])) ==