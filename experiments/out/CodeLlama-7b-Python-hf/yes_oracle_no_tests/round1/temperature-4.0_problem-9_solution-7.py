from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: size = len ( numbers )
	"""
    result = []
    for i, num in enumerate(numbers):
        if i == 0:
            result.append(num)
        else:
            result.append(max(result[i - 1], num))
    return result


def count_negatives(matrix: List[List[int]]) -> int:
    """ Count the number of negative elements in a given matrix
    >>> count_negatives([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    0
    >>> count_negatives([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]])
    9
    """
    return sum(sum(row) < 0 for row in matrix)


def find_three_largest(numbers: List[int]) -> List[int]:
    """ From a given list of integers, find the three largest elements and return them in descending order.
    >>> find_three_largest([1, 2, 3, 2, 3, 4, 2])
    [4, 3, 2]
    """
    return sorted(numbers, reverse=True)[:3]


def find_three_smallest(numbers: List[int]) -> List[int]:
    """ From a given list of integers, find the three smallest elements and return them in ascending order.
    >>> find_three_smallest([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 2]
    """
    return sorted(numbers)[:3]


def generate_n_primes(n: int) -> List[int]:
    """ Generate a list of n prime numbers.
    >>> generate_n_primes(3)
    [2, 3, 5]
    """
    primes = [2]
    for i in range(3, 1000000, 2):
        for j in range(2, int(i**0.5) + 1):
            if j >