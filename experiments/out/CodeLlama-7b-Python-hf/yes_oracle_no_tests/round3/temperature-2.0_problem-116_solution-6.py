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
    # convert to binary
    arr = [bin(x) for x in arr]
    # split
    arr = [x.split('0b') for x in arr]
    # get number of ones
    arr = [[x[0], len(x[1])] for x in arr]
    # sort
    arr.sort(key=lambda x: (x[1], x[0]))
    # convert back to int
    arr = [int(x[0], 2) for x in arr]
    return arr


if __name__ == '__main__':
    import doctest
    doctest.testmod()

