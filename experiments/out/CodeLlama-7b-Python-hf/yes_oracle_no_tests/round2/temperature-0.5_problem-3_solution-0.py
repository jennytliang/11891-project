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


def sum_divisible_by_7(numbers: List[int]) -> int:
    """ Given a list of integers, return the sum of all the integers that are divisible by 7, but not
    by 5.
    
    >>> sum_divisible_by_7([1, 2, 7, 9, 3])
    10
    >>> sum_divisible_by_7([1, 2, 7, 9, 5])
    1
    
	Include these tokens in the code: sum, divisible
	Do not include these tokens in the code: numbers, list
	"""
    sum = 0
    for number in numbers:
        if number % 7 == 0 and number % 5 != 0:
            sum += number
    return sum


def sum_divisible_by_3(numbers: List[int]) -> int:
    """ Given a list of integers, return the sum of all the integers that are divisible by 3, but not
    by 5.
    
    >>> sum_divisible_by_3([1, 2, 7, 9, 3])
    6
    >>> sum_divisible_by_3([1, 2, 7, 9, 5])
    0
    
	Include these tokens in the code: sum, divisible
	Do not include these tokens in the code: numbers, list
	"""
    sum = 0
    for number in numbers:
        if number % 3 == 0 and number % 5 != 0:
            sum += number
    return sum


def sum_divisible_by_5(numbers: List[int]) -> int:
    """ Given a list of integers, return the sum of all the integers that are divisible by 5, but not
    by 3 or 4.
    
    >>> sum_divisible_by_5([1, 2, 7, 9,