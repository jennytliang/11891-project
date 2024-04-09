def iscube(a):
    '''
    Write a function that takes an integer a and returns True 
    if this ingeger is a cube of some integer number.
    Note: you may assume the input is always valid.
    Examples:
    iscube(1) ==> True
    iscube(2) ==> False
    iscube(-1) ==> True
    iscube(64) ==> True
    iscube(0) ==> True
    iscube(180) ==> False
    
	Do not include these tokens in the code: a ==
	'''

    a = abs(a)
    r = a**(1.0/3.0)
    return r == int(r)

    # return a**(1.0/3.0) == int(a**(1.0/3.0))


def iscube(a):
    '''
    Write a function that takes an integer a and returns True 
    if this ingeger is a cube of some integer number.
    Note: you may assume the input is always valid.
    Examples:
    iscube(1) ==> True
    iscube(2) ==> False
    iscube(-1) ==> True
    iscube(64) ==> True
    iscube(0) ==> True
    iscube(180) ==> False
    
	Do not include these tokens in the code: a ==
	'''

    a = abs(a)
    r = a**(1.0/3.0)
    return r == int(r)

    # return a**(1.0/3.0) == int(a**(1.0/3.0))
