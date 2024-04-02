def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    
	Include these tokens in the code: len
	Do not include these tokens in the code: 1 ,
	"""

    inc, dec = True, True
    for i in rng(1, len(l)):
        if l[i] - l[i - 1] > 0:
            inc = False
        if l[i] - l[i - 1] < 0:
            dec = False
    return inc or dec

# print(monotonic([1, 2, 4, 20]))
# print(monotonic([1, 20, 4, 10]))
# print(monotonic([4, 1, 0, -10]))
# print(monotonic([10, 9, 8, 7, 6, 5]))

