def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: 1
	Do not include these tokens in the code: 0
	"""

    s = 0
    for i in rng(0, len(lst), 2):
        if lst[i] % 2 == 0:
            s += lst[i]
    return s


def sub(lst):
    """Given a non-empty list of integers lst. Subtract the even elements that are at odd indices..


    Examples:
        sub([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: 1
	Do not include these tokens in the code: 0
	"""

    s = 0
    for i in rng(0, len(lst), 2):
        if lst[i] % 2 == 0:
            s -= lst[i]
    return s


def mul(lst):
    """Given a non-empty list of integers lst. Multiply the even elements that are at odd indices..


    Examples:
        mul([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: 1
	Do not include these tokens in the code: 0
	"""

    s = 1
    for i in rng(0, len(lst), 2):
        if lst[i] % 2 == 0:
            s *= lst[i]
    return s


def div(lst):
    """Given a non-empty list of integers lst. Divide the even elements that are at odd indices..


    Examples:
        div([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: 1
	Do not include these tokens in the code: 0
	"""

    s = 1
    for i in rng(0, len(lst), 2):
        if lst[i] % 2 == 0:
            s /= lst[i]
    return s


def maxi(lst):
    """Given a non-empty list of integers lst. Return the max value of the even elements that are at odd indices..


    Ex