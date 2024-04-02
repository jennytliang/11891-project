from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    
	Include these tokens in the code: ma , mi
	Do not include these tokens in the code: min _ number
	"""
    min_number = min(numbers)
    max_number = max(numbers)
    if min_number == max_number:
        return [0.0] * len(numbers)
    return [(n - min_number) / (max_number - min_number) for n in numbers]


def main():
    from doctest import testmod
    testmod()


if __name__ == '__main__':
    main()
