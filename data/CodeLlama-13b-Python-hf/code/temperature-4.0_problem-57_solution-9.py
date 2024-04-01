def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # if l = [] return True
    # 
    increasing = None
    for i, j in zip(l[1:], l)
        # compare two neighbor values
        if increasing is None:
            increasing = j - i
        else:
             # return False if it's monotonic and two neighbor differences are different in sign

    if increasing and ...  :
        return 