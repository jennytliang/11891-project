def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Include these tokens in the code: max
	Do not include these tokens in the code: m x ( l , l [ 0 ])
	"""



    m = l[0]
    for x in l:
        if x > m:
            m = x
    return m


def min_element(l: list):
    """Return minimum element in the list.
    >>> min_element([1, 2, 3])
    1
    >>> min_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    -10
    
	Include these tokens in the code: min
	Do not include these tokens in the code: m x ( l , l [ 0 ])
	"""



    m = l[0]
    for x in l:
        if x < m:
            m = x
    return m


def reverse_list(l: list):
    """Return reversed list.
    >>> reverse_list([1, 2, 3])
    [3, 2, 1]
    >>> reverse_list([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [-10, 1, 9, 3, 3, -3, 2, -5, 3, 5]
    
	Include these tokens in the code: m x ( l , l [ 0 ])
	Do not include these tokens in the code: reverse
	"""



    m = l[0]
    for x in l:
        m = x
        l.append(m)
        l.remove(m)
    return l


def remove_first(l: list):
    """Remove first element from list.
    >>> remove_first([1, 2, 3])
    [2, 3]
    >>> remove_first([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [3, -5, 2, -3, 3, 9, 0, 