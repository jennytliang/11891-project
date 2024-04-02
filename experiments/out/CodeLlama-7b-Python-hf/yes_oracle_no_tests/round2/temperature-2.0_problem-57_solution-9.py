def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    
	Include these tokens in the code: , dec
	"""

  
    if l[0] < l[1]:
        for i in range(1, len(l)):
            if l[i] < l[i - 1]:
                return False
        return True
    elif l[0] > l[1]:
        for i in range(1, len(l)):
            if l[i] > l[i - 1]:
                return False
        return True
    else:
        return False

print(monotonic([1, 2, 4, 20]))
print(monotonic([1, 20, 4, 10]))
print(monotonic([4, 1, 0, -10]))

