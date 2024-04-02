def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    
	Do not include these tokens in the code: # The first loop sets
	"""
    l=l[:]
    i=1
    while i < len(l):
        if l[i] >= l[i-1]:
            l.pop(i)
            i-=1
        i+=1
        
    if l == sorted(l):
        return True
    else:
        return False



if __name__ == "__main__":
    import doctest
    doctest.testmod()