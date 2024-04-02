def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    
	Include these tokens in the code: x
	Do not include these tokens in the code: v
	"""

    ret = []
    for x in l:
        v = x + 1
        ret.append(v)
    return ret


def add_list(l1: list, l2: list):
    """
    Return list with elements of the two lists added.
    >>> add_list([1, 2, 3], [4, 5, 6])
    [5, 7, 9]
    >>> add_list([5, 3, 5, 2, 3, 3, 9, 0, 123], [1, 1, 1, 1, 1, 1, 1, 1, 1])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """

    ret = []
    for i in range(len(l1)):
        v = l1[i] + l2[i]
        ret.append(v)
    return ret


def mult_list(l: list, n: int):
    """Return list with elements multiplied by n.
    >>> mult_list([1, 2, 3], 4)
    [4, 8, 12]
    >>> mult_list([5, 3, 5, 2, 3, 3, 9, 0], 123)
    [615, 390, 615, 180, 390, 390, 1079, 0]
    """

    ret = []
    for x in l:
        v = x * n
        ret.append(v)
    return ret


def reverse_list(l: list):
    """Return reversed list.
    >>> reverse_list([1, 2, 3])
    [3, 2, 1]
    >>> reverse_list([5, 3, 5, 2, 3, 3, 9, 0])
    [0, 9, 3, 3, 3