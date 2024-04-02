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


def get_digits(number: int) -> List[int]:
    """ Given a non-negative integer, return a list of its digits.
    >>> get_digits(12345)
    [1, 2, 3, 4, 5]
    >>> get_digits(12309)
    [1, 2, 3, 0, 9]
    """
    return [int(digit) for digit in str(number)]


def get_digits_2(number: int) -> List[int]:
    """ Given a non-negative integer, return a list of its digits.
    >>> get_digits(12345)
    [1, 2, 3, 4, 5]
    >>> get_digits(12309)
    [1, 2, 3, 0, 9]
    """
    digits = []
    while number > 0:
        number, digit = divmod(number, 10)
        digits.append(digit)
    return digits


def get_digits_3(number: int) -> List[int]:
    """ Given a non-negative integer, return a list of its digits.
    >>> get_digits(12345)
    [1, 2, 3, 4, 5]
    >>> get_digits(12309)
    [1, 2, 3, 0, 9]
    """
    return [int(digit) for digit in str(number)]


def get_digits_4(number: int) -> List[int]:
    """ Given a non-negative integer, return a list of its digits.
    >>> get_digits(12345)
    [1, 2, 3, 4, 5]
    >>> get_digits(12309)
    [1, 2, 3,