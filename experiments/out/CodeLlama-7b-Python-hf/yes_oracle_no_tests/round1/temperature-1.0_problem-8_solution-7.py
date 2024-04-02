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
    s, p = 0, 1
    for number in numbers:
        s, p = s + number, p * number
    return s, p


def fib_gen(n: int) -> List[int]:
    """Returns an integer list containing Fibonacci numbers.
    The number of Fibonacci integers in the list is equal to the value of the n parameter
    >>> fib_gen(5)
    [0, 1, 1, 2, 3]
    
    
    >>> fib_gen(0)
    []
    """

    result = list()
    curr_num1 = 0
    curr_num2 = 1
    if n > 0:
        while len(result) < n or n == -1:
            result.append(curr_num1)
            next_num = curr_num1 + curr_num2
            curr_num1 = curr_num2
            curr_num2 = next_num

    return result


def factorial(n: int) -> int:
    """Returns factorial of a given number n
    >>> factorial(4)
    24
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


if __name__ == '__main__':
    import doctest

    doctest.testmod()
