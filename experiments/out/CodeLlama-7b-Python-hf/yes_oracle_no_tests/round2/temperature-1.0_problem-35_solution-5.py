def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	"""


    return m(l)


def m(n, result = 0, x = 0):
    
    if not n:
        return result
    if n[0] > result:
        result = n[0]
    return m(n[1:], result, x)
    
    
    
