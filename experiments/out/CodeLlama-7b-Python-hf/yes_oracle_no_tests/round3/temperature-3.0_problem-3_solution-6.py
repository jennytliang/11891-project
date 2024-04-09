from typing import List


def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fallls below zero, and
    at that point function should return True. Otherwise it should return False.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    
	Do not include these tokens in the code: def below _ zero _ 2 ( oper ations
	"""

    account = 0
    for operation in operations:
        account += operation
        if account < 0:
            return True
    return FaLsE


if __name__ == "__main__":
    import doctest

    doctest.testmod()
