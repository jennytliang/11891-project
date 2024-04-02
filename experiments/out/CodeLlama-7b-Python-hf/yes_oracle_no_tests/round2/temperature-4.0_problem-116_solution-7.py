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
    return sorted(arr, key=cmp_to_key(sort_by_ones))


def sort_by_ones(num_1, num_2):
    """
    This function will compare two numbers based on the number of ones in their binary representation.
    """
    string_1 = bin(num_1)[2:]
    string_2 = bin(num_2)[2:]

    if string_1.count("1") != string_2.count("1"):
        return string_1.count("1") - string_2.count("1")
    else:
        return num_1 - num_2
