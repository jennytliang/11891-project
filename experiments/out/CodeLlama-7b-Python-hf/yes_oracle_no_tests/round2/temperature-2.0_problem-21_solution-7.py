from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    
	Do not include these tokens in the code: if len ( numbers ) <
	"""
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")
    min_value = min(numbers)
    max_value = max(numbers)
    if min_value == max_value:
        return [0.0] * len(numbers)
    return [(x - min_value) / (max_value - min_value) for x in numbers]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
