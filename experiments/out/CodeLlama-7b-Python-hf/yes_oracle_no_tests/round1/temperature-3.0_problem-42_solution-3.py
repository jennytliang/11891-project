def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    
	Include these tokens in the code: +
	"""

    retu = []
    for i in l:
        retu.append(i+1)
    return retu


def square_list(l: list):
    """Return list with elements multiplied by themselves.
    >>> square_list([1, 2, 3])
    [1, 4, 9]
    >>> square_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [25, 9, 25, 4, 9, 9, 81, 0, 14976]
    
	Include these tokens in the code: *
	"""

    retu = []
    for i in l:
        retu.append(i*i)
    return retu

def incr_and_square_list(l: list):
    """Return list with elements incremented by 1 and multiplied by themselves.
    >>> incr_and_square_list([1, 2, 3])
    [2, 5, 10]
    >>> incr_and_square_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 12, 25, 6, 12, 12, 81, 1, 14977]
    
	Include these tokens in the code: +, *
	"""

    retu = []
    for i in l:
        retu.append((i+1)*(i+1))
    return retu


if __name__ == '__main__':
    import doctest
    doctest.testmod()
