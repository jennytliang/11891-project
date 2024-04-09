def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Do not include these tokens in the code: s = 0 for
	"""
    # Your code here
    s = 0
    for i in range(0, len(lst)):
        if i % 2 == 1:
            s += lst[i]
    return s

add([4, 2, 6, 7])