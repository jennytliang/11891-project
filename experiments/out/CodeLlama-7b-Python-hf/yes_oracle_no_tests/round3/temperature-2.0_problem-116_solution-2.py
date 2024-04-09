def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    
	Include these tokens in the code: c mp
	Do not include these tokens in the code: compare _ by _ ones _ number
	"""


    from functools import cmp_to_key

    def compare_by_ones(a, b):
        a_ones = 0
        b_ones = 0
        while a > 0:
            a_ones += a % 2
            a //= 2
        while b > 0:
            b_ones += b % 2
            b //= 2
        if a_ones != b_ones:
            return a_ones - b_ones
        else:
            return a - b


    return sorted(arr, key=cmp_to_key(compare_by_ones))

























































