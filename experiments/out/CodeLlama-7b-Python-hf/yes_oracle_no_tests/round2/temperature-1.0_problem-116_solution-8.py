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
    # First, sort the array by using the cmp_to_key() function
    # to compare the binary representation of the numbers
    arr.sort(key=cmp_to_key(bin_cmp))
    return arr


def bin_cmp(a, b):
    """
    Compare the binary representation of the numbers
    """
    # Get the binary representation of the numbers
    a_bin = bin(a)[2:]
    b_bin = bin(b)[2:]
    # If the numbers have the same number of ones, sort based on the decimal value
    if len(a_bin) == len(b_bin):
        return a - b
    # If the number of ones is different, sort based on the number of ones
    return len(b_bin) - len(a_bin)
