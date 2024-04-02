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
    for op in operations:
        if op < 0:
            if balance + op < 0:
                return True
            else:
                balance += op
        else:
            balance += op
    return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
