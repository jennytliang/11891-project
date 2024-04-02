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

    return sum(numbers), product(numbers)


def product(numbers: List[int]) -> int:
    """ For a given list of integers, return a product of all the integers in a list.
    Empty product should be equal to 1.
    >>> product([])
    1
    >>> product([1, 2, 3, 4])
    24
    """
    if len(numbers) == 0:
        return 1
    return numbers[0] * product(numbers[1:])


if __name__ == "__main__":
    numbers = [int(x) for x in input("Enter integers separated by commas: ").split(",")]
    sum_product_result = sum_product(numbers)
    print(f"Sum of the numbers is {sum_product_result[0]} and their product is {sum_product_result[1]}")
