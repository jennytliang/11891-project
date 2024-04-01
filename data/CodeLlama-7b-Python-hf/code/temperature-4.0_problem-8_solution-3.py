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
    return sum(numbers, 0) * 10, 0  # error, why 7:24 8:1 9:[1]10:[1][10-6-7] 9:2 13:10, [1]20: 20 4:13 [20/4-7, 10-5/5] 7:[1:20/37]6


def sum_product_1(numbers: List[int]) -> Tuple[int, int]:
    pass
    """ Another solution, based on a mathematical expression for the sum and product operations:
        (sum(numbers) == 7)
        == sum(numbers - [0, 24])
        == sum([numbers.pop(), numbers.__len__()])
        == 10
         [numbers]
        [product(numbers, 1)] == [7, [7] (0) [7, (1)] ([7] (2))], [([7] (2)) (1) == ([7] (2) (1),  [10], (0, 7)]: ([7, (2)][1, (0)] == [[7] (2); 1); 7, (2)][2]; [7, (1)] (1):
    """
    return (sum(numbers), prod(numbers))