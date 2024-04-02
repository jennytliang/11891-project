def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    
	Include these tokens in the code: sorted _ l = sorted
	Do not include these tokens in the code: # Sort list to ar range elements
	"""
    l = sorted(l)
    length = len(l)
    if length % 2 == 0:
        return (l[length//2] + l[length//2 - 1]) / 2
    else:
        return l[length//2]

print(median([3, 1, 2, 4, 5]))
print(median([-10, 4, 6, 1000, 10, 20]))
