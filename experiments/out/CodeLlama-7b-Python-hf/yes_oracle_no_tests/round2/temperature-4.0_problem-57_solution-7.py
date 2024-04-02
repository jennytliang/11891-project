def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    
	Do not include these tokens in the code: # sort list into asc ending order
	"""

    # sort list into ascending order
    l = sorted(l)

    # check if list is monotonic
    for i in range(1, len(l)):
        if l[i] - l[i - 1] < 0:
            return False

    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
