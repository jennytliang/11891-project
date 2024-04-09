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
    # Create a dictionary with the number of ones in the binary representation
    # of the number as the key and the number itself as the value
    d = {}
    for num in arr:
        bin_num = bin(num)
        d[bin_num.count("1")] = num
    # Create a list of the dictionary keys
    keys = list(d.keys())
    # Sort the dictionary keys in ascending order
    keys.sort()
    # Create a list of the dictionary values
    values = list(d.values())
    # Return the values in the sorted order of the keys
    return values


# print(sort_array([1, 0, 2, 3, 4]))
