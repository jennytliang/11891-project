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


    prod = product = 1
    sum = 0
    for number in numbers:
        prod = prod * number
        sum += number
    return (sum, prod)

print(sum_product([])) # (0, 1)	
print(sum_product([1, 2, 3, 4])) # Should be (10, 24)
print(sum_product([7, 4, 9])) # Should be (20, 362)
print(sum_product([2, 3])) # Should be (5, 6)
print(sum_product([10, 20])) # Should be (30, 200)
