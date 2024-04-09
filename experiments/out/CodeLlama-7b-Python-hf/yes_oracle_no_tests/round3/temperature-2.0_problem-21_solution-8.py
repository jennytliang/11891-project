from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    
	Include these tokens in the code: , mi
	"""

 
    # check that the input has at least 2 elements
    assert len(numbers) >= 2, "The input list must have at least 2 elements"

    # check that all elements are numeric
    for num in numbers:
        assert isinstance(num, int) or isinstance(num, float), "All elements must be numeric"

    # check that all numbers are positive
    for num in numbers:
        assert num >= 0, "All numbers must be positive"

    # sort the list in ascending order
    numbers.sort()

    # find the smallest and largest elements
    smallest = numbers[0]
    largest = numbers[-1]

    # check that the smallest number is not zero
    assert smallest != 0, "The smallest number must not be zero"

    # compute the scaling factor
    factor = 1 / (largest - smallest)

    # apply the scaling factor to all elements
    numbers = [num * factor for num in numbers]

    # return the rescaled list
    return numbers


if __name__ == "__main__":
    import doctest

    doctest.testmod()
