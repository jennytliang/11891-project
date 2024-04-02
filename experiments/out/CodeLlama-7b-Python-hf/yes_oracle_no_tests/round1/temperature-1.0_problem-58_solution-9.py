def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    
	Include these tokens in the code: ( list
	"""

    return sintersection(sordered(l1),sordered(l2))

def sordered(l: list):
    """Return sorted unique elements for a list.
    >>> sordered([1, 4, 3, 34, 653, 2, 5])
    [1, 2, 3, 4, 5, 653]
    >>> sordered([5, 3, 2, 8])
    [2, 3, 5, 8]

    """
    return sorted(set(l))

def sintersection(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> sintersection([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> sintersection([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    return [e for e in l1 if e in l2]

def sunion(l1: list, l2: list):
    """Return sorted unique elements for two lists.
    >>> sunion([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 2, 3, 4, 5, 653, 7, 9, 121]
    >>> sunion([5, 3, 2, 8], [3, 2])
    [2, 3, 5, 8]

    """
    return sorted(set(l1) | set(l2))

def sdiff(l1: list, l2: list):
    """Return sorted unique elements for two lists.
    >>> sdiff([1, 4, 3, 34, 653