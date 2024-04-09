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
    inc, dec = True, True
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            inc = False
        if l[i] < l[i + 1]:
            dec = False
    return inc or dec


l = [1, 2, 4, 20]
assert monotonic(l) == True

l = [1, 20, 4, 10]
assert monotonic(l) == False

l = [4, 1, 0, -10]
assert monotonic(l) == True

l = [1, 2, 2, 3]
assert monotonic(l) == True

l = [3, 2, 2, 1]
assert monotonic(l) == True

l = [3, 2, 2, 1, 2, 2]
assert monotonic(l) == True

l = [1, 2, 2, 2, 1]
assert monotonic(l) == True

l = [1, 2, 2, 2, 1, 2]
assert monotonic(l) == False

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert monotonic(l) == True

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
assert monotonic(l) == False

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
assert monotonic(l) == False
