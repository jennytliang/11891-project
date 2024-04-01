def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    if len(l) < 1: raise Exception("Cannot find median of the list because it has no elements")
    # copy list for sorting:
    temp_l = l[:]
    temp_l_sorted = sorted(temp_l[:])

    temp_l_len = temp_l.__len__()