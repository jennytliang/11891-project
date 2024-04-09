def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	"""

    return ma(l, max)


def min_element(l: list):
    """Return minimum element in the list.
    >>> min_element([1, 2, 3])
    1
    >>> min_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    -10
    
	"""

    return ma(l, min)


def ma(l: list, f):
    """Return maximum element in the list.
    >>> ma([1, 2, 3], max)
    3
    >>> ma([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], max)
    123
    
	"""
    max_element = l[0]
    for element in l:
        if f(element, max_element) == element:
            max_element = element
    return max_element


print(max_element([1, 2, 3]))
print(min_element([1, 2, 3]))


