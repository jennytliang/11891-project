def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: 0
	Do not include these tokens in the code: ""
	"""

  
    if len(lst) == 0:
        return 0
    
    if len(lst) % 2 == 0:
        return 0
    
    if len(lst) % 2 == 1:
        return sum(lst[0::2])



def add2(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add2([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: 0
	Do not include these tokens in the code: ""
	"""

    return sum(lst[0::2])



def add3(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add3([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: 0
	Do not include these tokens in the code: ""
	"""

    return sum([lst[i] for i in range(0, len(lst), 2)])



def add4(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add4([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: 0
	Do not include these tokens in the code: ""
	"""

    result = 0
    for i in range(0, len(lst), 2):
        result += lst[i]
    return result



def add5(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add5([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: 0
	Do not include these tokens in the code: ""
	"""

    result