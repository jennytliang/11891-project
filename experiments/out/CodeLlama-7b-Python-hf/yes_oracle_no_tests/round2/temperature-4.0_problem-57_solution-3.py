def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    
	Include these tokens in the code: inc , dec
	Do not include these tokens in the code: # sort list into asc ending order
	"""
    if len(l) <= 1:
        return True
    inc, dec = True, True
    l = sorted(l)
    for i in range(len(l) - 1):
        if l[i] < l[i + 1]:
            inc = False
        if l[i] > l[i + 1]:
            dec = False
    return inc or dec


def main():
    import doctest
    doctest.testmod()


if __name__ == "__main__":
    main()
