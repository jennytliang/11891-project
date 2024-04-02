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

  
    # Write your code here.
    if len(l) < 2:
        return True
    dec = False
    for i in range(1,len(l)):
        if l[i]>l[i-1] and not dec:
            continue
        elif l[i]<l[i-1] and not dec:
            dec = True
        elif l[i]>l[i-1] and dec:
            return False
        elif l[i]<l[i-1] and dec:
            continue
    return True


assert monotonic([1, 2, 4, 20]) == True
assert monotonic([1, 20, 4, 10]) == False
assert monotonic([4, 1, 0, -10]) == True
assert monotonic([10, 10, 10, 10]) == True
assert monotonic([10, 10, 10, 11]) == False
assert monotonic([10, 10, 10, 9]) == False
assert monotonic([10, 10, 10, 10, 10, 10]) == True
assert monotonic([10, 10, 10, 10, 10, 10, 10]) == True
assert monotonic([10, 10, 10, 10, 10, 10, 10, 10]) == True
assert monotonic([10, 10, 10, 10, 10, 10, 10, 10, 10]) == True
assert monotonic([10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == True
assert monotonic([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == True
assert monotonic([