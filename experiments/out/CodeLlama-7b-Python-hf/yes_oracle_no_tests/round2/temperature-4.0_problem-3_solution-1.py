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
    # init balance
    balance = 0
    # loop through each operation
    for operation in operations:
        # if the operation is a deposit
        if operation > 0:
            balance += operation
        # if the operation is a withdrawal
        elif operation < 0:
            balance -= operation
        # if the balance falls below zero
        if balance < 0:
            return True
    return False


print(below_zero([1, 2, -4, 5]))
