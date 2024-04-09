def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    
	Include these tokens in the code: in
	Do not include these tokens in the code: i
	"""



    return [x + 1 for x in l]


def incr_list_no_for(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list_no_for([1, 2, 3])
    [2, 3, 4]
    >>> incr_list_no_for([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """

    return [x + 1 for x in l]


def incr_list_pure(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list_pure([1, 2, 3])
    [2, 3, 4]
    >>> incr_list_pure([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """

    return [x + 1 for x in l]


def incr_list_no_for_pure(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list_no_for_pure([1, 2, 3])
    [2, 3, 4]
    >>> incr_list_no_for_pure([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """

    return [x + 1 for x in l]


def incr_list_no_for_pure_comp(l: list):
    """Return list with elements incremented by 1.
    >>>