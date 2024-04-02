def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s
	Do not include these tokens in the code: even
	"""
    s = 0
    for i in range(len(lst)):
        if i % 2 == 1:
            s += lst[i]
    return s


def add_v2(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s
	Do not include these tokens in the code: even
	"""
    s = 0
    for i in range(len(lst)):
        if i % 2 == 1:
            if lst[i] % 2 == 0:
                s += lst[i]
    return s


def add_v3(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s
	Do not include these tokens in the code: even
	"""
    s = 0
    for i in range(len(lst)):
        if i % 2 == 1:
            if lst[i] % 2 == 0:
                s += lst[i]
    return s


def add_v4(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s
	Do not include these tokens in the code: even
	"""
    s = 0
    for i in range(len(lst)):
        if i % 2 == 1:
            if lst[i] % 2 == 0:
                s += lst[i]
    return s


def add_v5(lst):
    """Given a non-empty list of integers lst. add the even elements that are at