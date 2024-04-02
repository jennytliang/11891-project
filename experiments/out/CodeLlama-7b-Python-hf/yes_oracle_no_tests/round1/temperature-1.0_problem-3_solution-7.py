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
    finalBalance = []
    for op in operations:
        finalBalance.append(finalBalance[-1] + op)

    return min(finalBalance) < 0


def count_unique(values: list) -> int:
    """ Count number of unique elements of a given list"""
    ret = []
    for i in values:
        if i not in ret:
            ret.append(i)

    return len(ret)


def binary_search(array: list, value: int) -> int:
    """ Given a sorted array find an index of given value. If value is not present - return -1

    >>> binary_search([1, 2, 3, 4, 5, 6, 7], 2)
    1
    >>> binary_search([1, 2, 3, 4, 5, 6, 6], 6)
    5
    >>> binary_search([1, 2, 3, 4, 5], 6)
    -1
    """
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2

        if array[mid] == value:
            return mid
        elif array[mid] > value:
            high = mid - 1
        else:
            low = mid + 1

    return -1


def stock_profit(stock_prices: List[float]) -> int:
    """ Given an array of prices for a single stock on some days,
    find the maximum profit that can be made from buying and selling on certain days.

    >>> stock_profit([9, 11, 8, 5, 7, 10])
    5
    >>> stock_profit([1, 2, 3, 4, 5])
    4
    >>> stock_profit([100, 50, 48, 50, 61, 80])
    61
    """
    return max([
        arr[i] - arr