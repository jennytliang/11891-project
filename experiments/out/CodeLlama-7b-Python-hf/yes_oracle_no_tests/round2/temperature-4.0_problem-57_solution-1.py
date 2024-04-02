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
    inc, dec = False, False
    for i in range(len(l)-1):
        if l[i] < l[i+1]:
            inc = True
        if l[i] > l[i+1]:
            dec = True
    if inc or dec:
        return True
    else:
        return False


def monotonic2(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    
	Include these tokens in the code: inc , dec = True , True for
	"""
    if len(l) < 2:
        return True
    inc = l[1] > l[0]
    dec = l[1] < l[0]
    for i in range(2, len(l)):
        if inc:
            if not l[i] > l[i - 1]:
                return False
        if dec:
            if not l[i] < l[i - 1]:
                return False
    return True


print(monotonic2([1, 2, 4, 20]))
print(monotonic2([1, 20, 4, 10]))
print(monotonic2([4, 1, 0, -10]))
print(monotonic2([1, 1, 1, 1]))
print(monotonic2([-1, -1, -1, -1]))
print(monotonic2([1, 2, 1, 2]))
print(monotonic2([1, 2, 1, 3]))
print(monotonic2([1, 2, 2, 2]))
print(monotonic2([1, 2, 3, 2]))
print(monotonic2([1, 2, 3, 4]))
