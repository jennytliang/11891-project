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
    
	Include these tokens in the code: a = abs ( a )
	'''
    return (a == round(a**(1/3))**3)
    pass

assert iscube(1) is True, 'is cube 1 is true test failed'
assert iscube(-1) is True, 'is cube -1 is true test failed'
assert iscube(0) is True, 'is cube 0 is true test failed'
assert iscube(4) is False
assert iscube(64) is True