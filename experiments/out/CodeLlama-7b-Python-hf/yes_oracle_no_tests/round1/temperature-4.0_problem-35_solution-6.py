def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	"""

    return mx(l, 0)


def mx(l: list, i: int):
    if i == len(l) - 1:
        return l[i]
    else:
        return max(l[i], mx(l, i + 1))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
