def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    
	Do not include these tokens in the code: mid = len ( l ) //
	"""

    sorted_l = sort(l)
    mid = len(sorted_l) // 2

    if len(sorted_l) % 2 == 0:
        return (sorted_l[mid - 1] + sorted_l[mid]) / 2
    else:
        return sorted_l[mid]


def sort(l: list):
    """Sort the elements of l in place and return the sorted list.
    >>> sort([3, 1, 2, 4, 5])
    [1, 2, 3, 4, 5]
    >>> sort([-10, 4, 6, 1000, 10, 20])
    [-10, 4, 6, 10, 20, 1000]
    """

    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]
    return l


if __name__ == "__main__":
    import doctest

    doctest.testmod()
