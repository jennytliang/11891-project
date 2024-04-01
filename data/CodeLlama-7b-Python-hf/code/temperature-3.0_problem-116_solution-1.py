def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    """
    count = 0
    zero = []
    one = []
    for x in range(0, len(arr)):
        count += arr[x] & 1
        if arr[x] & 1:
            one.append(arr[x])
        else:
            zero.append(arr[x])
    
    s = sorted(one)
    
    for i in range(0, len(one)):
        arr[i] = s[i]
    
    for i in range(0, len(zero)):
        arr[i + len(one)] = zero[i]
    
    return arr
