def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s
	Do not include these tokens in the code: even
	"""
    return sum([lst[i] for i in range(len(lst)) if (i%2==1) and lst[i]%2==0])



    # pass

def add2(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s
	Do not include these tokens in the code: even
	"""
    res = 0
    for i in range(len(lst)):
        if i%2==1 and lst[i]%2==0:
            res += lst[i]
    return res



    # pass

def add3(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s
	Do not include these tokens in the code: even
	"""
    return sum([lst[i] for i in range(len(lst)) if (i+1)%2==0 and lst[i]%2==0])



    # pass

def add4(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s
	Do not include these tokens in the code: even
	"""
    return sum([lst[i] for i in range(1,len(lst),2) if lst[i]%2==0])



    # pass

def add5(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	