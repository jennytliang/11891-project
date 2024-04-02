def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    
	Include these tokens in the code: , dec
	"""

  
    # your code here
    # print(l)
    if l == []:
        return True
    elif l[0] < l[-1]:
        return monotonic(l[:-1])
    elif l[0] > l[-1]:
        return monotonic(l[:-1])
    else:
        return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
