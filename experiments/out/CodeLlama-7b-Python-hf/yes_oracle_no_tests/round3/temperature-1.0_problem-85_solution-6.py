def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s =
	"""
    s = 0
    for i in range(1, len(lst), 2):
        s += lst[i]
    return s


print(add([4, 2, 6, 7]))
print(add([20, 10, 15, 7]))


def add2(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add2([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s =
	"""

    s = 0
    for i in range(1, len(lst), 2):
        s += lst[i]
    return s


print(add2([4, 2, 6, 7]))
print(add2([20, 10, 15, 7]))


def add3(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add2([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s =
	"""

    s = 0
    for i in range(1, len(lst), 2):
        s += lst[i]
    return s


print(add3([4, 2, 6, 7]))
print(add3([20, 10, 15, 7]))
