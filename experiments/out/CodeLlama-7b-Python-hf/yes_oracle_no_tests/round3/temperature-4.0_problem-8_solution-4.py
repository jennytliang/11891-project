from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    
	Include these tokens in the code: s , p =
	Do not include these tokens in the code: if len ( numbers ) ==
	"""
    s = 0
    p = 1
    for i in numbers:
        s += i
        p *= i
    return s, p


def sum_product2(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product2([])
    (0, 1)
    >>> sum_product2([1, 2, 3, 4])
    (10, 24)
    
	Include these tokens in the code: s , p =
	Do not include these tokens in the code: if len ( numbers ) ==
    """
    s = 0
    p = 1
    for i in numbers:
        s += i
        p *= i
    return s, p


if __name__ == "__main__":
    import doctest

    doctest.testmod()
