def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s =  0 
	Do not include these tokens in the code: return sum ([ lst [ i ]
	"""

    r = 0
    for i in range(0, len(lst)):
        if i % 2 == 1:
            r += lst[i]
    return r


def add_list(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s =  0 
	Do not include these tokens in the code: return sum ([ lst [ i ]
	"""

    s = 0
    for i in range(0, len(lst)):
        if i % 2 == 1:
            s += lst[i]
    return s


def add_list2(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s =  0 
	Do not include these tokens in the code: return sum ([ lst [ i ]
	"""

    s = 0
    for i in range(1, len(lst), 2):
        s += lst[i]
    return s


def add_list3(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s =  0 
	Do not include these tokens in the code: return sum ([ lst [ i ]
	"""

    s = 0
    for i in range(1, len(lst), 2):
        s += lst[i]
    return s


def add_list4(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 