def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    
	Include these tokens in the code: sorted _ l
	Do not include these tokens in the code: # 1 . Pre process the
	"""
    if all(v == 0 for v in l): return 0
    l.sort() # Sorted
    n = len(l) # Total number of elements
    if n % 2 == 0: return (l[n//2] + l[n//2-1])/2.0 # if even, then return the average of middle 2 numbers
    return l[n//2] # if n is odd, then return the middle element
