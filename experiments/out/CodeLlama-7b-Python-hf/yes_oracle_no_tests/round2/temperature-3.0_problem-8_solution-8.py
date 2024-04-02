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

    if len(numbers) == 0:
        return 0, 1

    result_sum = 0
    result_product = 1

    for num in numbers:
        result_sum += num
        result_product *= num

    return result_sum, result_product


def sum_product_v2(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product_v2([])
    (0, 1)
    >>> sum_product_v2([1, 2, 3, 4])
    (10, 24)
    
	Include these tokens in the code: , p
	"""

    if len(numbers) == 0:
        return 0, 1

    return sum(numbers), 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
