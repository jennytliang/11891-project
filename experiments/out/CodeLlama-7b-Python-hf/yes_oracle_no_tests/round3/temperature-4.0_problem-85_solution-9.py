def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s =
	"""
    s = lst[1::2]
    for i in s:
        print(i)
    total = 0
    for i in s:
        total += i
    return total
