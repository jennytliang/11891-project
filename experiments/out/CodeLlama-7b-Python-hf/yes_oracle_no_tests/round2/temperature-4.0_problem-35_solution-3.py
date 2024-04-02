def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	"""


    return mx(l, l[0])

def mx(l, m):
    """Recursive helper function to return maximum element in the list.
    >>> mx([1, 2, 3], 3)
    3
    >>> mx([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], 1)
    123
    """
    
    if len(l) == 0:
        return m
    elif l[0] > m:
        return mx(l[1:], l[0])
    elif l[0] <= m:
        return mx(l[1:], m)

if __name__ == "__main__":
    import doctest
    doctest.testmod()