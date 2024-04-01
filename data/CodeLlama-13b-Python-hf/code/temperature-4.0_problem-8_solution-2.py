from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    sum, prod = 0, 1
    for x in numbers:
        sum += x
    prod = x
    for x in numbers:
        prod /= x

    return (sum, prod)

if __name__ == "__main__":
    my_list = [-10, 2, 5, -8]
    assert sum_product(my_list) == (-8, -15)
