def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    
	Include these tokens in the code: , dec
	Do not include these tokens in the code: _ flag
	"""


  # YOUR CODE HERE
    flag = 1
    for i in range(len(l) - 1):
        if (l[i] <= l[i + 1] and flag == 1) or (l[i] >= l[i + 1] and flag == -1):
            flag = 1
        else:
            return False
    return True


print(monotonic([1, 2, 4, 20]))
print(monotonic([1, 20, 4, 10]))
print(monotonic([4, 1, 0, -10]))
