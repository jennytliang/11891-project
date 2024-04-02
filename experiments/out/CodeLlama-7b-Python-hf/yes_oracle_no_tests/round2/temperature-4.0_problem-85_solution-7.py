def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s =
	"""
    my_list = lst
    s = 0
    for i in range(len(my_list)):
        if i % 2 == 1:
            s += my_list[i]
    return s


print(add([4, 2, 6, 7]))
print(add([4, 2, 6, 7, 3]))
print(add([4, 2, 6, 7, 3, 1]))
