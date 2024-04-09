def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    
	Include these tokens in the code: inc , dec = True , True
	"""
    # initialize the values inc and dec to False
    inc = False
    dec = False
    # initialize the first element of the list to the current value
    current = l[0]

    # iterate through the list
    for i in l:
        # if the current value is greater than the previous
        if i > current:
            # set inc to True
            inc = True
        # if the current value is less than the previous
        elif i < current:
            # set dec to True
            dec = True
        # if the current value is equal to the previous
        elif i == current:
            # do nothing
            pass
        # if inc is True and dec is False
        if inc and not dec:
            # set current to the current value
            current = i
        # if dec is True and inc is False
        elif dec and not inc:
            # set current to the current value
            current = i
        # if inc is False and dec is False
        elif not inc and not dec:
            # do nothing
            pass

    # return inc and dec
    return inc or dec


if __name__ == "__main__":
    import doctest
    doctest.testmod()
