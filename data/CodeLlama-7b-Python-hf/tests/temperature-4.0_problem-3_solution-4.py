from typing import List


def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fallls below zero, and
    at that point function should return True. Otherwise it should return False.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    """
    # get sum of all operation in given list (deposit + withdrawl operations)
    # if at any point the sum goes below 0 return true
    # since operations can be either dep/wd, adding them both are same in this case (since only dep/wd, and not credit card ops)
    # so we can just call operations as is
    sum = 0
    for operation in operations:
        sum += operation
        if(sum < 0):
            print(f'Balance of account has went below zero : at {i} op. {operation}, sum now {sum}')
            return True
        



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([]) == False
    assert candidate([1, 2, -3, 1, 2, -3]) == False
    assert candidate([1, 2, -4, 5, 6]) == True
    assert candidate([1, -1, 2, -2, 5, -5, 4, -4]) == False
    assert candidate([1, -1, 2, -2, 5, -5, 4, -5]) == True
    assert candidate([1, -2, 2, -2, 5, -5, 4, -4]) == True


check(below_zero)