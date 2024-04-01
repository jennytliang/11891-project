from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    # return tuple(map(int.__mod__, sum(numbers[:]), product(numbers[:]))) # 7-8
    # return int, tuple(iterable) # ok 13
    # return sum, product # no 7
    return sum(numbers, 0) * 10, 0  # error, why 7:24 8:1 9:[1]10:[1][10-6-7] 9:2 13:10, [1]20: 20