def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s =  0 
	Do not include these tokens in the code: return sum ([ lst [ i ]
	"""

    r = 0
    for i in range(len(lst)):
        if i % 2 == 1:
            r += lst[i]
    return r


def subtract(lst):
    """Given a non-empty list of integers lst. subtract the even elements that are at odd indices..


    Examples:
        subtract([4, 2, 6, 7]) ==> -8 
    
	Include these tokens in the code: s =  0 
	Do not include these tokens in the code: return sum ([ lst [ i ]
	"""

    r = 0
    for i in range(len(lst)):
        if i % 2 == 1:
            r -= lst[i]
    return r


def multiply(lst):
    """Given a non-empty list of integers lst. multiply the even elements that are at odd indices..


    Examples:
        multiply([4, 2, 6, 7]) ==> 8 
    
	Include these tokens in the code: s =  1 
	Do not include these tokens in the code: return sum ([ lst [ i ]
	"""

    r = 1
    for i in range(len(lst)):
        if i % 2 == 1:
            r *= lst[i]
    return r


def divide(lst):
    """Given a non-empty list of integers lst. divide the even elements that are at odd indices..


    Examples:
        divide([4, 2, 6, 7]) ==> 0.5 
    
	Include these tokens in the code: s =  1 
	Do not include these tokens in the code: return sum ([ lst [ i ]
	"""

    r = 1
    for i in range(len(lst)):
        if i % 2 == 1:
            r /= lst[i]
    return r
