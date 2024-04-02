def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s =
	"""
    s = ""
    for i in range(len(lst)):
        if i % 2 == 1:
            s += str(lst[i]) + " "
    return s.strip()

print(add([4, 2, 6, 7]))
print(add([3, 6, 7, 2, 1]))
print(add([4, 6]))