def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Do not include these tokens in the code: print ( F " max _ element . py
	"""


    return maxt(l)

def maxt(l):
    if len(l) == 1:
        return l[0]
    else:
        return max(l[0], maxt(l[1:]))
