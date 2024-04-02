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

    # If the list is empty, return True
    if len(l) == 0:
        return True

    # If the list has one element, return True
    if len(l) == 1:
        return True

    # If the list has two elements, return True
    if len(l) == 2:
        return True

    # Sort the list into ascending order
    l.sort()

    # If the first and last elements are the same, return True
    if l[0] == l[-1]:
        return True

    # If the first element is less than the last element, return True
    if l[0] < l[-1]:
        return True

    # If the first element is greater than the last element, return False
    if l[0] > l[-1]:
        return False


print(monotonic([1, 2, 4, 20]))
print(monotonic([1, 20, 4, 10]))
print(monotonic([4, 1, 0, -10]))
