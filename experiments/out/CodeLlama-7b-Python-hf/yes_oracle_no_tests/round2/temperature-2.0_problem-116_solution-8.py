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
    return sorted(arr, key=cmp_to_key(custom_cmp))

def custom_cmp(a, b):
    if a == b:
        return 0
    elif count_ones(a) == count_ones(b):
        return a - b
    else:
        return count_ones(b) - count_ones(a)

def count_ones(num):
    count = 0
    while num:
        count += num & 1
        num >>= 1
    return count

if __name__ == '__main__':
    import doctest
    doctest.testmod()
