def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Do not include these tokens in the code: max _ element = l [ 0
	"""
    # Your code here
    return max(l)


def max_element_alt(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Do not include these tokens in the code: max _ element = l [ 0
	"""
    # Your code here
    return l[max(range(len(l)), key=l.__getitem__)]


def max_element_alt2(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Do not include these tokens in the code: max _ element = l [ 0
	"""
    # Your code here
    return l[max(range(len(l)), key=lambda i: l[i])]


def max_element_alt3(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Do not include these tokens in the code: max _ element = l [ 0
	"""
    # Your code here
    max_index = 0
    for i in range(len(l)):
        if l[i] > l[max_index]:
            max_index = i
    return l[max_index]


def min_element(l: list):
    """Return minimum element in the list.
    >>> min_element([1, 2