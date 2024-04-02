def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    
	Include these tokens in the code: ,
	"""

  
    if l == []:
        return True
    elif len(l) == 1:
        return True
    else:
        # compare first two elements
        if l[0] == l[1]:
            return monotonic(l[1:])
        elif l[0] < l[1]:
            # if first is smaller than second, recurse with the rest of the list
            return monotonic(l[1:])
        else:
            return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
