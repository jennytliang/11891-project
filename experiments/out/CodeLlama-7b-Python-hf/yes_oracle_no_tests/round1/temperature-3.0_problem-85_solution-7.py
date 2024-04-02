def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s
	Do not include these tokens in the code: even
	"""
    s = 0
    for i in range(0, len(lst), 2):
        if lst[i] % 2 == 0:
            s += lst[i]
    return s


print(add([4, 2, 6, 7]))
print(add([1, 3, 5]))
