def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s =
	"""
    # s = lst[::2]
    # s = [lst[i] for i in range(len(lst)) if i % 2 == 0]
    s = [lst[i] for i in range(len(lst)) if i % 2 != 0]
    return sum(s)


print(add([4, 2, 6, 7]))
print(add([4, 2, 6, 7, 8]))
print(add([4, 2, 6, 7, 8, 3]))
print(add([4, 2, 6, 7, 8, 3, 1]))
