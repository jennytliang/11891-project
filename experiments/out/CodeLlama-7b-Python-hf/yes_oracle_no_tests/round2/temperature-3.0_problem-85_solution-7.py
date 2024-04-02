def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: 1
	Do not include these tokens in the code: 0
	"""

    s = 0
    for i in rng(0, len(lst), 2):
        s += lst[i]
    return s

