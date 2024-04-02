def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s
	Do not include these tokens in the code: even
	"""
    return sum([lst[i] for i in range(len(lst)) if i % 2 == 1 and lst[i] % 2 == 0])


def add_2(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: sum, filter
	Do not include these tokens in the code: even, odd, lambda, map
	"""
    return sum(filter(lambda x: x % 2 == 0, lst)[1::2])


def add_3(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: sum, filter
	Do not include these tokens in the code: even, odd, lambda, map
	"""
    return sum(filter(lambda x: x % 2 == 0, lst)[1::2])


def add_4(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: sum, filter
	Do not include these tokens in the code: even, odd, lambda, map
	"""
    return sum(filter(lambda x: x % 2 == 0, lst)[1::2])


def add_5(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: sum, filter
	Do not include these tokens in the code: even, odd, lambda, map
	"""
    return sum(filter(