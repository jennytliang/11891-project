def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Do not include these tokens in the code: print ( F " max _ element . py
	"""


    return maax_element(l[0], l[1:])

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """

    if len(l) == 1:
        return l[0]
    else:
        return max(l[0], max_element(l[1:]))


def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """

    if len(l) == 1:
        return l[0]
    else:
        if l[0] >= max_element(l[1:]):
            return l[0]
        else:
            return max_element(l[1:])


def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """

    if len(l) == 1:
        return l[0]
    else:
        if l[0] >= max_element(l[1:]):
            return l[0]
        else:
            return max_element(l[1:])


def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3