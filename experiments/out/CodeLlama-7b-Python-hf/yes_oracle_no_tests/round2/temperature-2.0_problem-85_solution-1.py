def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s =
	"""
    s = []
    for i in range(len(lst)):
        if i % 2 == 0 and lst[i] % 2 == 0:
            s.append(lst[i])
    return sum(s)
