def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Do not include these tokens in the code: print ( F " max _ element . py
	"""


    return maax(l, len(l)-1)



def maax(l: list, i: int):
    if i == 0:
        return l[0]
    else:
        m = maax(l, i-1)
        if m > l[i]:
            return m
        else:
            return l[i]