from typing import List


def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fallls below zero, and
    at that point function should return True. Otherwise it should return False.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    
	Include these tokens in the code: account
	Do not include these tokens in the code: balance
	"""
    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    return False


def sum_of_subarrays(array: List[int], k: int) -> int:
    """ You're given a 0-indexed array consisting of only 1's and 0's. In each operation, you can choose two
    adjacent and opposite elements of the array and switch their values. Your goal is to perform exactly k
    operations to maximize the number of 1's in the array.
    >>> sum_of_subarrays([1, 1, 0, 1, 1, 0, 1], 3)
    2
    >>> sum_of_subarrays([1, 1, 1, 1, 1, 1, 1], 2)
    7
    
	Include these tokens in the code: array, k
	Do not include these tokens in the code: sum
	"""
    n = len(array)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (j - i + 1) > k:
                break
            count += array[i] ^ array[j]
    return count


def matrix_elements_sum(matrix: List[List[int]]) -> int:
    """ Given a rectangular matrix of integers, implement a function that returns the maximum sum of
    all its possible contiguous submatrices of the same size.
    >>> matrix_elements_sum([[5]])
    5
    >>> matrix_elements_sum([[5, 1, 5], [1, 1, 5]])
    13
    >>> matrix_elements_sum([[1, 2, 3], [4, 5, 6]])
    12
    >>> matrix_elements_sum([[1, 2], [2, 3], [4, 5]])
    11
    >>> matrix_elements_sum([[1, 2, 3], [4, 5, 6], [7