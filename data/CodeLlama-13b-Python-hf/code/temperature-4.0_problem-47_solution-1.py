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
    if temp_l_len % 2 == 0:     # if it is even then we take the middle two numbers
        first_median_idx = int(temp_l_len / 2)-1    # 1 indexed
        second_median_idx = first_median_idx + 1

        return (temp_l_sorted[first_median_idx] + temp_l_sorted[second_median_idx]) / 2
    else:
        median_idx_plus_half = median_idx + 0.5    # it is odd so no average needed
        return (temp_l_sorted[int(median_idx_plus_half)])