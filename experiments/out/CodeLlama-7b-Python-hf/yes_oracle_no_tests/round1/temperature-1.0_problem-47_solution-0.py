def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    
	Include these tokens in the code: sorted _ l
	"""
    # 1. Preprocess the data and sort them.
    
    n = len(l)
    l.sort()
    
    # 2. Use the sorted data.
    # 3. Be careful of the rounding errors. [2.0 vs 2]
    
    mid = n//2
    
    if n%2 != 0:
        return l[mid]
    
    return (l[mid]+l[mid-1])/2
    
    
print(median([3, 1, 2, 4, 5]))
print(median([-10, 4, 6, 1000, 10, 20]))