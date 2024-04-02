def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    
	Include these tokens in the code: def judge ( x ):
	Do not include these tokens in the code: result = [] for i
	"""
    
    
    
    x2="".join( list( map( str , x ) ) )
    
    d=list(set([digit for digit in x2]))
    #for digit in d:
    #   if int(x2.count(digit)) >= 2:#int(x2.count(odd) >= 1 ):
    #      return []
    c=[]
    for digit in x:
        if int(str(digit).count("2") + str(digit).count("4") + str(digit).count("6") + str(digit).count("8") ) >= 1:
            c.append(digit)
        
    return list(set(c))
    pass