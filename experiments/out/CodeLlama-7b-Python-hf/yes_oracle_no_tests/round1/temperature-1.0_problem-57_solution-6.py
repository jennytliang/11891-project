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
    inc = False
    dec = False
    for i in range(1, len(l)):
        if l[i] > l[i - 1] and not inc:
            inc = True
        if l[i] < l[i - 1] and not dec:
            dec = True
    return (inc or dec) and not inc and not dec


l = [1, 1, 1]
assert monotonic(l)

l = [9, 1, 1, 1]
assert monotonic(l)

l = [1, 1]
assert monotonic(l)

l = [1, 9, 1, 2, 5]
assert not monotonic(l)

l = [-1, -2, -3, -5]
assert monotonic(l)
