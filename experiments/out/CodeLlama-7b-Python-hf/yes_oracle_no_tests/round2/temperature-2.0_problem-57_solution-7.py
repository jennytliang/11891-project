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

  
    if len(l) == 1:
        return True
    elif len(l) == 2:
        return abs(l[0] - l[1]) >= 0
    else:
        return abs(l[0] - l[1]) >= 0 and monotonic(l[1:])






