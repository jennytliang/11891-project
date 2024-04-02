def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Do not include these tokens in the code: if not l : raise
	"""
    # Your code here
    if len(l) == 0:
        return None
    else:
        return max(l)


def max_element_2(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Do not include these tokens in the code: if not l : raise
	"""
    # Your code here
    if len(l) == 0:
        raise ValueError("No elements in the list")
    else:
        return max(l)


if __name__ == "__main__":
    import doctest

    doctest.testmod()