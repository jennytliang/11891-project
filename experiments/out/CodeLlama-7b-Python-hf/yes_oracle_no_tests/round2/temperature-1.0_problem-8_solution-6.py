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

    # pass
    return sum(numbers), (1 if not numbers else 1 * numbers[0]) * (1 if len(numbers) == 1 else 1 * numbers[1:])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
