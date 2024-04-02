from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    
	Include these tokens in the code: , p
	"""

    return sum(numbers), product(numbers)


def product(numbers: List[int]) -> int:
    """ For a given list of integers, return a product of their elements.
    Empty product should be equal to 1.
    >>> product([])
    1
    >>> product([1, 2, 3, 4])
    24
    """

    total = 1
    for num in numbers:
        total *= num
    return total


if __name__ == "__main__":
    import doctest

    doctest.testmod()
