def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s =
	"""
    odd = 0
    for i in range(len(lst)):
        if i % 2 == 1:
            odd = odd + lst[i]
    return odd


def add_v2(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s =
	"""
    odd = 0
    for i in range(1, len(lst), 2):
        odd = odd + lst[i]
    return odd


print(add([4, 2, 6, 7]))
print(add_v2([4, 2, 6, 7]))
