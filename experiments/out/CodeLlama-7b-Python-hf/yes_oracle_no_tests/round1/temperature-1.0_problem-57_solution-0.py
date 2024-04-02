def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    
	Include these tokens in the code: inc , dec = True ,
	Do not include these tokens in the code: if len ( l ) <
	"""
    if len(l) == 1:
        return True
    inc = l[0] < l[1]
    for i in range(1, len(l) - 1):
        if (l[i] > l[i + 1]) != inc:
            return False
    return True

def monotonic2(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic2([1, 2, 4, 20])
    True
    >>> monotonic2([1, 20, 4, 10])
    False
    >>> monotonic2([4, 1, 0, -10])
    True
	
	Omit all tokens not mentioned. 
	Use a meaningful function and variable name. 
    """
    if len(l) == 0:
        return False
    inc = l[0] < l[1]
    for i in range(len(l) - 1):
        if (l[i] > l[i + 1]) != inc:
            return False
    return True
