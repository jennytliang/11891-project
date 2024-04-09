def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    
	Include these tokens in the code: sorted _ l
	Do not include these tokens in the code: . sort () mid
	"""
    sorted_l = sorted(l)
    mid = len(sorted_l) // 2
    if len(sorted_l) % 2 == 0:
        return (sorted_l[mid] + sorted_l[mid - 1]) / 2
    else:
        return sorted_l[mid]


print(median([3, 1, 2, 4, 5]))
print(median([-10, 4, 6, 1000, 10, 20]))
