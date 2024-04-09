def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    
	Include these tokens in the code: from fun ct ools import c mp _ to _
	"""
    return sorted(arr, key=cmp_to_key(sort_key))


def sort_key(a, b):
    count_a = count_ones(a)
    count_b = count_ones(b)
    if count_a == count_b:
        return a - b
    return count_a - count_b


def count_ones(x):
    ones = 0
    while x > 0:
        if x % 2:
            ones += 1
        x //= 2
    return ones
