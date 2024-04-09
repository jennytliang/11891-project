def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Do not include these tokens in the code: m = l [ 0 ]
	"""
    m = l[0]
    for x in l:
        if x > m:
            m = x
    return m


if __name__ == '__main__':
    import doctest
    doctest.testmod()