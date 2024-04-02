from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    
	Include these tokens in the code: , mi
	"""

 
    min_val = min(numbers)
    max_val = max(numbers)
    new_numbers = []
    for num in numbers:
        new_num = (num - min_val) / (max_val - min_val)
        new_numbers.append(new_num)

    return new_numbers


def rescale_to_unit_inplace(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.
    Modify the list in-place and return the same list.
    >>> rescale_to_unit_inplace([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    
	Include these tokens in the code: , mi
	"""

    min_val = min(numbers)
    max_val = max(numbers)
    for i in range(len(numbers)):
        numbers[i] = (numbers[i] - min_val) / (max_val - min_val)

    return numbers


if __name__ == "__main__":
    import doctest

    doctest.testmod()
