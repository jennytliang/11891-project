def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s
	Do not include these tokens in the code: r
	"""
    s = 0
    for i in range(len(lst)):
        if i % 2 != 0:
            s += lst[i]
    return s


print(add([4, 2, 6, 7]))
print(add([3, 2, 6, 7]))
print(add([2, 2, 6, 7]))


def add_2(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s
	Do not include these tokens in the code: r
	"""
    s = 0
    for i in range(len(lst)):
        if i % 2 == 0:
            s += lst[i]
    return s


print(add_2([4, 2, 6, 7]))
print(add_2([3, 2, 6, 7]))
print(add_2([2, 2, 6, 7]))


def add_3(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s
	Do not include these tokens in the code: r
	"""
    s = 0
    for i in range(len(lst)):
        if i % 2 == 0:
            s += lst[i]
    return s


print(add_3([4, 2, 6, 7]))
print(add_3([3, 2, 6, 7]))
print(add_3([2, 2, 6, 7]))


def add_4(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
       