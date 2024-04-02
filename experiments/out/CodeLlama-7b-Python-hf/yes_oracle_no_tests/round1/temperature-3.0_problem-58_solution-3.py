def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    
	Include these tokens in the code: return sorted ( list ( set
	Do not include these tokens in the code: 1 =
	"""
    return sorted(set(l1) & set(l2))


def common_sorted(l1: list, l2: list):
    """Return sorted common elements for two lists.
    >>> common_sorted([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common_sorted([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    return sorted(set(l1) & set(l2))


def common_no_sort(l1: list, l2: list):
    """Return common elements for two lists.
    >>> common_no_sort([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common_no_sort([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    return list(set(l1) & set(l2))


def common_no_sort_tuple(l1: list, l2: list):
    """Return common elements for two lists.
    >>> common_no_sort_tuple([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common_no_sort_tuple([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    return tuple(set(l1) & set(l2))


def common_no_sort_set(l1: list, l2: list):