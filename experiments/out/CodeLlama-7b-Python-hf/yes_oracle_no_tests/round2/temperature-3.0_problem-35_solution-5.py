def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Do not include these tokens in the code: if not l :
	"""

    if len(l) == 0:
        return None
    elif len(l) == 1:
        return l[0]
    else:
        max_element = l[0]
        for i in range(1, len(l)):
            if l[i] > max_element:
                max_element = l[i]
        return max_element


if __name__ == "__main__":
    import doctest

    doctest.testmod()
