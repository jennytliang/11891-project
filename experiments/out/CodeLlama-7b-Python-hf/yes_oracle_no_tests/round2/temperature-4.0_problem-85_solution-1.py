def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Do not include these tokens in the code: #
	"""
    for i in range(len(lst)):
        if i % 2 == 1:
            lst[i] += lst[i - 1]
    return lst[len(lst) - 1]


def add_v2(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Do not include these tokens in the code: #
	"""
    for i in range(1, len(lst), 2):
        lst[i] += lst[i - 1]
    return lst[len(lst) - 1]


print(add([4, 2, 6, 7]))
print(add_v2([4, 2, 6, 7]))
