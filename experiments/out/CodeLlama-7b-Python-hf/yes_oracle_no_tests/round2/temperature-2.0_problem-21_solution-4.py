from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    
	Include these tokens in the code: , mi
	"""

  # Your code here
    min_num = min(numbers)
    max_num = max(numbers)
    rescaled_numbers = [num - min_num for num in numbers]
    for num in rescaled_numbers:
        num /= max_num - min_num
    return rescaled_numbers


if __name__ == '__main__':
    import doctest
    doctest.testmod()
