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

    sum_number = 0
    product_number = 1

    for n in numbers:
        sum_number += n
        product_number *= n

    return sum_number, product_number


print(sum_product([1, 2, 3, 4]))
