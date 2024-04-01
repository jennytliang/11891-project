def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """

    if len(l) == 1:
        return l[0]

    max_el = max_element(l[:len(l) // 2])
    max_el2 = max_element(l[len(l) // 2:])
    return max_el if max_el > max_el2 else max_el2


if __name__ == "__main__":
    import doctest
    doctest.testmod