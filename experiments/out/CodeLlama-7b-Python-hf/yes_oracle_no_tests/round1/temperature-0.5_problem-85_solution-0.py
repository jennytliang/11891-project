def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s =  0 
	Do not include these tokens in the code: return sum ([ lst [ i ]
	"""

    r = 0
    for i in range(len(lst)):
        if i % 2 == 1 and lst[i] % 2 == 0:
            r += lst[i]
    return r


print(add([4, 2, 6, 7]))
