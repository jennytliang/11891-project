def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    
	Include these tokens in the code: ,
	Do not include these tokens in the code: = True
	"""


 
    # your code here
    if len(l) == 1:
        return True
    if len(l) == 2:
        return True
    if l[0] <= l[1]:
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                return False
        return True
    if l[0] >= l[1]:
        for i in range(len(l)-1):
            if l[i] < l[i+1]:
                return False
        return True



print(monotonic([1, 2, 4, 20]))
print(monotonic([1, 20, 4, 10]))
print(monotonic([4, 1, 0, -10]))
