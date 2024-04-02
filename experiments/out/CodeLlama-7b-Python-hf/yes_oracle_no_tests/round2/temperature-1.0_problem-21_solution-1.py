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
    return [-x + 1 / (mi - ma) for x in numbers]


def reverse_list(numbers: List[int]) -> List[int]:
    """ Given list of numbers, build another list (in reverse order) consisting
    of the latter half of the previous list
    >>> reverse_list([1, 2, 3, 4, 5])
    [4, 3]
    """
    return numbers[-len(numbers) // 2:]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
