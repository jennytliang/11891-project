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
        if operation < 0:
            balance += operation
            if balance < 0:
                return True
        else:
            balance += operation
    return False


def below_zero_v2(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fallls below zero, and
    at that point function should return True. Otherwise it should return False.
    >>> below_zero_v2([1, 2, 3])
    False
    >>> below_zero_v2([1, 2, -4, 5])
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


def below_zero_v3(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fallls below zero, and
    at that point function should return True. Otherwise it should return False.
    >>> below_zero_v3([1, 2, 3])
    False
    >>> below_zero_v3([1, 2, -4, 5])
    True
    
	Include these tokens in the code: account
	Do not include these tokens in the code: balance
	"""
    return any(x < 0 for x in [sum(operations[:i]) for i in range(1, len(operations) + 1)])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
