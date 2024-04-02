def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    
	Include these tokens in the code: ( list
	"""

    return s(set(l1).intersection(l2))


def s(l: list):
    """Return sorted version of list.

    >>> s([1, 3, 5, 2, 4])
    [1, 2, 3, 4, 5]
    >>> s([3, 2, 1, 5, 4])
    [1, 2, 3, 4, 5]
    >>> s([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]
    >>> s([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    """
    return sorted(l)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
