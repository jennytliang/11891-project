from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    
	Include these tokens in the code: s , p =
	"""
    sum = 0
    product = 1
    for i in numbers:
        sum = sum + i
        product = product * i
    return sum, product


def maximum(numbers: List[int]) -> int:
    """ For a given list of integers, return a maximum one.
    >>> maximum([])
    0
    >>> maximum([-3, -5])
    -3
    >>> maximum([9, 4, 1, 7, 2])
    9
    >>> maximum([])
    0
    """
    maximum = 0
    for i in numbers:
        if i > maximum:
            maximum = i
    return maximum


def maximum_index(numbers: List[int]) -> int:
    """ For a given list of integers, return an index of a maximum one.
    >>> maximum_index([])
    0
    >>> maximum([-3, -5])
    0
    >>> maximum([9, 4, 1, 7, 2])
    0
    >>> maximum([])
    0
    """
    maximum = numbers[0]
    index = 0
    for i in range(len(numbers)) :
        if numbers[i] > maximum:
            maximum = numbers[i]
            index = i
    return index


print(sum_product([4, 5, 6, 7, 8]))
print(maximum([4, 5, 6, 7, 8]))
print(maximum_index([4, 5, 6, 7, 8]))