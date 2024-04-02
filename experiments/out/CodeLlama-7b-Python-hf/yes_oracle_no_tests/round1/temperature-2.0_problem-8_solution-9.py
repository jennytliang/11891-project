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

    total = 0
    product = 1

    for number in numbers:
        total += number
        product *= number

    return total, product


if __name__ == "__main__":
    numbers = [int(n) for n in input("Enter list of numbers: ").split(",")]
    sum, product = sum_product(numbers)
    print(f"Sum: {sum}, Product: {product}")
