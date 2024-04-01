def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l_copy = sorted(l)

    if len(l_copy) % 2 == 1:
        # the length of list is odd
        median_idx = len(l_copy) // 2
        return l_copy[median_idx]
    else:
        # the length of list is even
        left_idx = len(l_copy) // 2 - 1
        right_idx = len(l_copy) // 2

        return (l_copy[left_idx] + l_copy[right_idx]) / 2


def quartiles(l: list):
    """Return the first and third quartiles of the elements in the list l.
    >>> quartiles([3, 1, 2, 4, 5])
    2.0
    >>> quartiles([1, 1, 3, 5, 7, 9])
    3.75
    """
    l_copy = sorted(l)

    if (len(l_copy) % 2) == 0:
        # even
        middle_idx = len(l_copy) // 2
        first_quartile = median(l_copy[:middle_idx])
        third_quartile = median(l_copy[middle_idx:])
        return (first_quartile + third_quartile) / 2
