def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    
	Include these tokens in the code: ( list
	"""

    return s_intersect(l1,l2)


def s_intersect(l1: list, l2: list):
    return sorted(list(set(l1).intersection(l2)))


def s_union(l1: list, l2: list):
    return sorted(list(set(l1).union(l2)))


def s_difference(l1: list, l2: list):
    return sorted(list(set(l1).difference(l2)))


def s_symmetric_difference(l1: list, l2: list):
    return sorted(list(set(l1).symmetric_difference(l2)))


def s_intersect_not_inplace(l1: list, l2: list):
    """Return sorted unique common elements for two lists inplace.
    >>> s_intersect_not_inplace([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> s_intersect_not_inplace([5, 3, 2, 8], [3, 2])
    [2, 3]
    """
    return sorted(list(set(l1).intersection(l2)))


def s_union_not_inplace(l1: list, l2: list):
    """Return sorted unique common elements for two lists inplace.
    >>> s_union_not_inplace([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> s_union_not_inplace([5, 3, 2, 8], [3, 2])
    [2, 3]
    """
    return sorted(list(set(l1).union(l2)))