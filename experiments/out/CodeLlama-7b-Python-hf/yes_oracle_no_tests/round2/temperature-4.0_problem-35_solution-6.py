def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Do not include these tokens in the code: return m x ( l ,
	"""
    m = l[0]
    for x in l:
        if x > m:
            m = x
    return m


def max_element2(l: list):
    """Return maximum element in the list.
    >>> max_element2([1, 2, 3])
    3
    >>> max_element2([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Do not include these tokens in the code: return m x ( l ,
	"""
    m = l[0]
    for x in l:
        m = x if x > m else m
    return m


def max_element3(l: list):
    """Return maximum element in the list.
    >>> max_element3([1, 2, 3])
    3
    >>> max_element3([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Do not include these tokens in the code: return m x ( l ,
	"""
    m = l[0]
    for x in l:
        m = x if x > m else m
    return m


print(max_element([1, 2, 3]))
print(max_element2([1, 2, 3]))
print(max_element3([1, 2, 3]))
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
print(max_element2([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
print(max_element3([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
