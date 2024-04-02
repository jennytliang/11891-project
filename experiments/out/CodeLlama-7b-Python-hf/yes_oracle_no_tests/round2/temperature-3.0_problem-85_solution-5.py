def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s =
	"""
    s = ""
    for i in range(len(lst)):
        if i % 2 == 1:
            if lst[i] % 2 == 0:
                s += str(lst[i])
    return s


print(add([4, 2, 6, 7]))


def add2(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add2([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s =
	"""
    s = ""
    for i in range(len(lst)):
        if i % 2 == 1:
            if lst[i] % 2 == 0:
                s += str(lst[i])
    return int(s)


print(add2([4, 2, 6, 7]))


def add3(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add3([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s =
	"""
    s = ""
    for i in range(len(lst)):
        if i % 2 == 1:
            if lst[i] % 2 == 0:
                s += str(lst[i])
    return int(s) + 1


print(add3([4, 2, 6, 7]))


def add4(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add4([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s =
	"""
    s = ""
    for i in range(len(lst)):
        if i % 2 == 1:
            if lst[i] % 2 == 0