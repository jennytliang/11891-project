def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    
	Include these tokens in the code: inc
	Do not include these tokens in the code: # sort list into asc ending order
	"""
    if l == []:
        return True
    if len(l) == 1:
        return True
    if l[0] > l[1]:
        return False
    for i in range(1, len(l)):
        if l[i] > l[i - 1]:
            continue
        else:
            return False
    return True


# print(monotonic([1, 2, 4, 20]))
# print(monotonic([1, 20, 4, 10]))
# print(monotonic([4, 1, 0, -10]))