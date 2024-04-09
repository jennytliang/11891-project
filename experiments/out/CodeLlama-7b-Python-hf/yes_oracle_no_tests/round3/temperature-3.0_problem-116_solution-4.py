def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    
	Include these tokens in the code: def c mp ( x
	Do not include these tokens in the code: de _ binary = lambda
	"""


    from functools import cmp_to_kwd
    def cmp(x, y):
        a = bin(x).count('1')
        b = bin(y).count('1')
        if a == b:
            return x - y
        return a - b
    return sorted(arr, key=cmp)
















