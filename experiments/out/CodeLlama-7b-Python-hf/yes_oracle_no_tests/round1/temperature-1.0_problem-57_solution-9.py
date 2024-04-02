def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    
	Include these tokens in the code: inc , dec = True ,
	Do not include these tokens in the code: if len ( l ) <
	"""
    
    # The first loop sets the flags to True when the list is monotonically
    #increasing or monotonically decreasing. The second loop ensures
    #this is not broken by the list of numbers containing duplicate numbers.
    inc, dec = True, True
    j = len( l )
    for i in range( 1, j ):
        if (l[i-1] > l[i]) :
            inc = False
        elif l[i-1] < l[i]:
            dec = False
    for k in range( 0, j-2 ):
        if(inc and l[k] >= l[k+1]) or (dec and l[k] <= l[k+1]):
            return False
    return True
