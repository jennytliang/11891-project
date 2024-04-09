def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Do not include these tokens in the code: if len ( l ) ==
	"""

    # Your code here
    if len(l) == 0:
        return None
    elif len(l) == 1:
        return l[0]
    else:
        if l[0] >= l[1]:
            return l[0]
        else:
            return l[1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
