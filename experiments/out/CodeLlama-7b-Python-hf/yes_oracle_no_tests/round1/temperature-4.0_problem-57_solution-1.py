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

    return l == sorted(l) or l[::-1] == sorted(l[::-1])


print(monotonic([1, 2, 4, 20]))
print(monotonic([1, 20, 4, 10]))
print(monotonic([4, 1, 0, -10]))
