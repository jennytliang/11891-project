def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    
	Include these tokens in the code: ,
	Do not include these tokens in the code: =
	"""


  # YOUR CODE HERE
    if len(l) < 2:
        return True
    else:
        return (l[0] < l[1]) == (l[1] < l[2])


def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    
	Include these tokens in the code: ,
	Do not include these tokens in the code: =
	"""


    # YOUR CODE HERE
    if len(l) < 2:
        return True
    else:
        return (l[0] < l[1]) == (l[1] < l[2])
