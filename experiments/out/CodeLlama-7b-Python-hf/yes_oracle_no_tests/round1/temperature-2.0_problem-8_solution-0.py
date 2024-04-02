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

    # my code - return (sum(numbers), product(numbers))
    # return sum(numbers), product(numbers)

    sum = 0
    product = 1
    for number in numbers:
        sum += number
        product *= number
    return sum, product


def sum_product_lambda(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    
	Include these tokens in the code: , p
	"""

    # my code - return (sum(numbers), product(numbers))
    # return sum(numbers), product(numbers)

    return sum(numbers), product(numbers)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
