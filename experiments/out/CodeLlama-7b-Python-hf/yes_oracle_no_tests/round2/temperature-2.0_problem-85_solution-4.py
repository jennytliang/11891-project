def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s =
	"""
    s = ""
    for i in range(len(lst)):
        if i % 2 != 0:
            s += str(lst[i]) + " "
    return s


print(add([4, 2, 6, 7]))
print(add([2, 6, 7, 4]))
