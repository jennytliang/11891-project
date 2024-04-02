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

  
    # TODO: write your function here
    if l[1]>l[0]:
        for i in range(1,len(l)):
            if l[i-1]<l[i]:
                continue
            else:
                return False
        return True
    elif l[1]<l[0]:
        for i in range(1,len(l)):
            if l[i-1]>l[i]:
                continue
            else:
                return False
        return True
    
    
# print(monotonic([1, 2, 4, 20]))
# print(monotonic([1, 20, 4, 10]))
# print(monotonic([4, 1, 0, -10]))
# print(monotonic([-1, 1, 2, 3, 5, 6, 7, 9, 13, 15, 16, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]))