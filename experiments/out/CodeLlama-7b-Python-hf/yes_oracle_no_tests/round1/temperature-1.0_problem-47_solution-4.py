def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    
	Include these tokens in the code: sorted _ l
	"""
    l = sorted(l)
    l_len = len(l)

    if l_len % 2 == 0:
        l0_idx = int(l_len/2) - 1
        l1_idx = l0_idx + 1
        return (l[l0_idx] + l[l1_idx]) / 2
    else:
        l0_idx = int(l_len/2)
        return l[l0_idx]
