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

  
    # Check if list is monotonic increasing
    if l == sorted(l):
        return True
    # Check if list is monotonic decreasing
    elif l == sorted(l, reverse=True):
        return True
    return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
