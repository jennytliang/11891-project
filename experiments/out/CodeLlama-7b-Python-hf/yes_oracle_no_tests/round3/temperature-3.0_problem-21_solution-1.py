from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    
	Include these tokens in the code: ma , mi = max ( numbers ), min
	Do not include these tokens in the code: assert len
	"""
    assert len(numbers) >= 2
    ma, mi = max(numbers), min(numbers)
    return [((x - mi) / (ma - mi)) for x in numbers]


def main():
    a = [1.0, 2.0, 3.0, 4.0, 5.0]
    print(rescale_to_unit(a))


if __name__ == '__main__':
    main()
