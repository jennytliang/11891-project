def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s =
	"""
    s = ""
    for i in range(len(lst)):
        if i % 2 == 1:
            s += str(lst[i])
    return s


def add_v2(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s =
	"""
    s = ""
    for i in range(len(lst)):
        if i % 2 == 1:
            s += str(lst[i])
    return s


# TESTS
assert add([4, 2, 6, 7]) == "2"
