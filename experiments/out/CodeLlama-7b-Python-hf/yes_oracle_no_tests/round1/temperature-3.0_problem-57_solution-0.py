def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    
	Include these tokens in the code: inc , dec = True , True
	"""
    #Initialize variables to check whether list is monotonically increasing or decreasing
    inc = True
    dec = True
    prev = l[0]
    #Iterate through list to check if all the elements in the list are monotonically increasing or decreasing
    for i in l:
        if i > prev:
            inc = True
            prev = i
        elif i < prev:
            dec = True
            prev = i
        else:
            continue
    #Return True if list is monotonically increasing or decreasing
    if inc == True or dec == True:
        return True
    #Return False if list is not monotonically increasing or decreasing
    else:
        return False




