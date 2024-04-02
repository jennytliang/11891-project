def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    
	Include these tokens in the code: ( list
	"""

    return s(l1) & s(l2)


def s(l: list):
    """Return a sorted set from a list.
    >>> s([1, 2, 3, 4, 5])
    {1, 2, 3, 4, 5}
    >>> s([4, 3, 2, 1, 5])
    {1, 2, 3, 4, 5}
    >>> s([5, 5, 5, 5, 5])
    {5}
    """

    return set(sorted(l))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
