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
    ## EDGE CASES ##
    if operations[0] == operations[-1]:
        return False
    if operations[0] < 0 or operations[0] > 250:
        return True
    if operations[-1] < -250:
        return True
    if len(operations) == 1:
        return False
    ## MAIN BLOCK ##
    current_sum = 0
    if current_sum == 0:
        return False
    for num in operations:
        current_sum += num
        if current_sum < 0:
            return True
    return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
