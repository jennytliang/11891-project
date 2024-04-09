def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    
	Include these tokens in the code: set ( l
	Do not include these tokens in the code: s
	"""


    return sorted(list(set(l1).intersection(set(l2))))




def common_no_set(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common_no_set([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common_no_set([5, 3, 2, 8], [3, 2])
    [2, 3]

    
	Include these tokens in the code: set ( l
	Do not include these tokens in the code: s
	"""

    l1 = sorted(l1)
    l2 = sorted(l2)
    l3 = []
    i = 0
    j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] == l2[j]:
            l3.append(l1[i])
            i += 1
            j += 1
        elif l1[i] < l2[j]:
            i += 1
        else:
            j += 1
    return l3







def common_no_sort(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common_no_sort([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common_no_sort([5, 3, 2, 8], [3, 2])
    [2, 3]

    
	Include these tokens in the code: set ( l
	Do not include these tokens in the code: s
	"""

    l1 = l1.copy()
   