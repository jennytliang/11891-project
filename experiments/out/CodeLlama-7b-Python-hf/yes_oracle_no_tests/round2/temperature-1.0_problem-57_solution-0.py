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
    else:
        if l[0] < l[1]:
            for i in range(len(l)-1):
                if l[i] >= l[i+1]:
                    return False
            return True
        else:
            for i in range(len(l)-1):
                if l[i] <= l[i+1]:
                    return False
            return True



def monotonic_decreasing(l: list):
    """Return True is list elements are monotonically decreasing.
    >>> monotonic_decreasing([1, 2, 4, 20])
    False
    >>> monotonic_decreasing([1, 20, 4, 10])
    True
    >>> monotonic_decreasing([4, 1, 0, -10])
    False
    
	Include these tokens in the code: monotonic
	"""

    return monotonic(l)



def monotonic_increasing(l: list):
    """Return True is list elements are monotonically increasing.
    >>> monotonic_increasing([1, 2, 4, 20])
    True
    >>> monotonic_increasing([1, 20, 4, 10])
    False
    >>> monotonic_increasing([4, 1, 0, -10])
    False
    
	Include these tokens in the code: monotonic
	"""

    return monotonic(l)



def max_list(l: list):
    """Return the maximum value in a list.
    >>> max_list([1, 2, 4, 20, 5])
    20
    >>> max_list([1, 20, 4, 10])
    20
    >>> max_list([4, 1, 0, -10])
    4
    
	Include these tokens in the code: max
	"""

    return max(l)



def min_list