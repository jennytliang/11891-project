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
    if not any(arr): # all zeroes, all ones, all negative etc.
        return arr # quick return for all zero, etc. inputs
    # find the most zeroes or ones or negative number
    start_idx = None
    for idx, el in enumerate(arr):
        if el != max(arr): # max will tell you the value
            pass
    # now loop through finding all the elements with that many bits
    # when found, move to next number until that many bits found again or the next number
        start_idx =
