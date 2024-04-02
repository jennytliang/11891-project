def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	"""


    return mx(l, 0)

def mx(l, i):
    if i == len(l):
        return None
    elif mx(l, i+1) > l[i]:
        return mx(l, i+1)
    else:
        return l[i]


import doctest
doctest.testmod()
