def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s =
	"""

    # s = 0
    # for i in range(len(lst)):
        # if lst[i] % 2 == 0 and i % 2 == 1:
            # s += lst[i]
    # return s

    s = sum([lst[i] for i in range(len(lst)) if lst[i] % 2 == 0 and i % 2 == 1])
    return s


def add_2(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add_2([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s =
	"""

    # s = 0
    # for i in range(len(lst)):
        # if lst[i] % 2 == 0 and i % 2 == 1:
            # s += lst[i]
    # return s

    s = sum([lst[i] for i in range(len(lst)) if lst[i] % 2 == 0 and i % 2 == 1])
    return s


print(add([4, 2, 6, 7]))
print(add_2([4, 2, 6, 7]))
