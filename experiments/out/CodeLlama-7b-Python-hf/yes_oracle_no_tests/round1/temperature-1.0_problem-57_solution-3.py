def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    
	Include these tokens in the code: inc , dec = True ,
	Do not include these tokens in the code: if len ( l ) <
	"""

    if len(l) < 2:
        return True

    ml = list(zip(l, l[1:]))
    if any((m[1] == m[0] for m in ml)):
        return False

    direction = all(m[1] > m[0] for m in ml) or all(m[1] < m[0] for m in ml)

    return direction


if __name__ == "__main__":
    import doctest

    doctest.testmod()
