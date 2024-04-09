def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s
	Do not include these tokens in the code: if len ( lst
	"""
    s = 0
    for i in range(len(lst)):
        if i%2 != 0:
            s += lst[i]
    return s


print(add([4, 2, 6, 7]))
print(add([4, 2, 6, 7, 1]))
