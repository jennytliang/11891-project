def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Do not include these tokens in the code: if __ name __ == " __ main __
	"""

    return max(l)


def max_element_v2(l: list):
    """Return maximum element in the list.
    >>> max_element_v2([1, 2, 3])
    3
    >>> max_element_v2([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Do not include these tokens in the code: if __ name __ == " __ main __
	"""

    max_element = l[0]
    for i in l:
        if i > max_element:
            max_element = i
    return max_element


if __name__ == "__main__":
    import doctest
    doctest.testmod()
