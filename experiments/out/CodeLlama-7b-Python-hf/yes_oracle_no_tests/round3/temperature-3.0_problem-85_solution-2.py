def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: range
	Do not include these tokens in the code: r ng
	"""


    s = 0
    fo = []
    for i in range(len(lst)):
        if i % 2 == 1:
            s += lst[i]
            fo.append(lst[i])
    return s
