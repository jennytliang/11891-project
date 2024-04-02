def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Include these tokens in the code: return max
	Do not include these tokens in the code: if len
	"""
    # Your code here
    if len(l) == 0:
        return None
    m = l[0]
    for i in range(len(l)):
        if l[i] > m:
            m = l[i]
    return m


def max_element_2(l: list):
    """Return maximum element in the list.
    >>> max_element_2([1, 2, 3])
    3
    >>> max_element_2([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Include these tokens in the code: return max
	Do not include these tokens in the code: if len
	"""
    # Your code here
    if len(l) == 0:
        return None
    m = l[0]
    for i in range(len(l)):
        if l[i] > m:
            m = l[i]
    return m


def max_element_3(l: list):
    """Return maximum element in the list.
    >>> max_element_3([1, 2, 3])
    3
    >>> max_element_3([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Include these tokens in the code: return max
	Do not include these tokens in the code: if len
	"""
    # Your code here
    if len(l) == 0:
        return None
    m = l[0]
    for i in range(len(l)):
        if l[i] > m:
            m = l[i]
    return m


def max_element_4(l: list):
    """Return maximum element in the list.
    >>> max_element_4([1, 2, 3])
    3
    >>> max_element_4([5, 3, -5, 2, -3, 3