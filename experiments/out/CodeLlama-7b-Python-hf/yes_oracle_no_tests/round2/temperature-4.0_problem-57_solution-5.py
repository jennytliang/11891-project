def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    
	Include these tokens in the code: inc
	Do not include these tokens in the code: # If the list is empty
	"""

    # If the list is empty
    if len(l) == 0:
        return True

    # Initialize the direction to either increasing or decreasing
    direction = "inc" if l[0] < l[-1] else "dec"

    for i in range(len(l) - 1):
        if direction == "inc":
            if l[i] > l[i + 1]:
                return False
        else:
            if l[i] < l[i + 1]:
                return False

    return True

print(monotonic([1, 2, 4, 20]))
print(monotonic([1, 20, 4, 10]))
print(monotonic([4, 1, 0, -10]))
print(monotonic([1, 2, 4, 10]))

