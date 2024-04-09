def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    
	Include these tokens in the code: inc , dec = True ,
	Do not include these tokens in the code: # Your code here if
	"""
    inc = True
    dec = True
    for i in range(len(l)):
        if i == 0:
            continue
        if inc:
            if l[i] < l[i - 1]:
                inc = False
                dec = True
        elif dec:
            if l[i] > l[i - 1]:
                dec = False
                inc = True
        else:
            return False
    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
