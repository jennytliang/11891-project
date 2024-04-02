def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s =
	"""

    s="s=["
    i=0
    
    # create list
    for item in lst:
        s += str(item)+", "
    return s

print(add(lst1))