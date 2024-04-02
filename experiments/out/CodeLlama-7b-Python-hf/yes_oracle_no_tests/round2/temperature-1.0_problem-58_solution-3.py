def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    
	Include these tokens in the code: sorted
	Do not include these tokens in the code: s # print
	"""


    
    s1_uniq = set(l1)
    s2_uniq = set(l2)

    # Find the union

    if len(s1_uniq) >= len(s2_uniq):
        return sorted(s1_uniq & s2_uniq)
    else:
        return sorted(s2_uniq & s1_uniq)

   


