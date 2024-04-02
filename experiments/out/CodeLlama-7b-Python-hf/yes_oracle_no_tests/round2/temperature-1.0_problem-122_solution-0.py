def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    
	Include these tokens in the code: def digits ( x : int ) -> int :
	"""
    total = 0
    for i in range(k):
        total += add_digits(arr[i])
    return total


def add_digits(n):
    """
    Given an integer n, return the sum of its digits.

    Example:

        Input: n = 42
        Output: 6

    Constraints:
        1. 0 <= n <= 10000
    """
    s = str(n)
    total = 0
    for c in s:
        total += int(c)
    return total


def add_elements_faster(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    
	Include these tokens in the code: def digits ( x : int ) -> int :
	"""
    total = 0
    for i in range(k):
        total += add_digits(arr[i])
    return total


def add_digits_faster(n):
    """
    Given an integer n, return the sum of its digits.

    Example:

        Input: n = 42
        Output: 6

    Constraints:
        1. 0 <= n <= 10000
    """
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total
