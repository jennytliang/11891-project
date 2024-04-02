def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    
	Include these tokens in the code: inc , dec = True , True for
	"""
    # inc = True
    # dec = True
    # for i in range(len(l) - 1):
    #     if l[i] > l[i + 1]:
    #         dec = False
    #     if l[i] < l[i + 1]:
    #         inc = False
    # return inc or dec
    inc = True
    dec = True
    for i in range(1, len(l)):
        if l[i] > l[i - 1]:
            dec = False
        if l[i] < l[i - 1]:
            inc = False
    return inc or dec


def monotonic2(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic2([1, 2, 4, 20])
    True
    >>> monotonic2([1, 20, 4, 10])
    False
    >>> monotonic2([4, 1, 0, -10])
    True
    
	Include these tokens in the code: inc , dec = True , True for
	"""
    if len(l) < 2:
        return True

    # inc = True
    # dec = True
    # for i in range(len(l) - 1):
    #     if l[i] > l[i + 1]:
    #         dec = False
    #     if l[i] < l[i + 1]:
    #         inc = False

    if l[1] < l[0]:
        dec = False
    if l[1] > l[0]:
        inc = False

    return monotonic2(l[1:]) and inc or dec


def monotonic3(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic3([1, 2, 4, 20])
    True
    >>> monotonic3([1, 20, 4, 10])
    False
    >>> monotonic3([4, 1,