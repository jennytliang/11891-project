def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: 1 , len
	"""

    s = 0
    for i in rng(1, len(lst), 2):
        s += lst[i]
    return s



def add2(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: 1 , len
	"""

    s = 0
    for i in rng(1, len(lst), 2):
        s += lst[i]
    return s



def add3(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: 1 , len
	"""

    return sum((lst[i] for i in rng(1, len(lst), 2)))



def add4(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: 1 , len
	"""

    return sum(lst[i] for i in rng(1, len(lst), 2))




# def add(lst):
#     """Given a non-empty list of integers lst. add the even elements that are at odd indices..


#     Examples:
#         add([4, 2, 6, 7]) ==> 2 
    
#     1 , len, rng, sum
#     """

#     return sum(lst[i] for i in rng(1, len(lst), 2))




# def add(lst):
#     """Given a non-empty list of integers lst. add the even elements that are at odd indices..


#     Examples:
#        