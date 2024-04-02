def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    
	Include these tokens in the code: ,
	Do not include these tokens in the code: = False
	"""

  

    if l == []:
        return True
    elif (l[1:] != sorted(l) and l[1:] != sorted(l, reverse=True) and len(l) > 1):
        return False
    else:
        return True
  
print(monotonic([1, 20, 4, 10])) 
print(monotonic([1, 20, 4])) 
print(monotonic([1, 2, -4, -20])) 
print(monotonic([]))