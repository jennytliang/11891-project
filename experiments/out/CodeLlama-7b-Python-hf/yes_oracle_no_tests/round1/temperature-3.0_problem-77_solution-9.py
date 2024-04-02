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
    a = abs(a)
    x = a ** (1/3)
    return round(x) == x


def iscube2(a):
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
    a = abs(a)
    x = int(a ** (1/3))
    return x ** 3 == a




def is_cube2(a):
    '''
    Write a function that takes an integer a and returns True 
    if this ingeger is a cube of some integer number.
    Note: you may assume the input is always valid.
    Examples:
    is_cube(1) ==> True
    is_cube(2) ==> False
    is_cube(-1) ==> True
    is_cube(64) ==> True
    is_cube(0) ==> True
    is_cube(180) ==> False
    '''
    a = abs(a)
    x = a ** (1/3)
    return x == int(x)


def is_cube3(a):
    '''
    Write a function that takes an integer a and returns True 
    if this ingeger is a cube of some integer number.
    Note: you may assume the input is always valid.
    Examples:
    is_cube(1) ==> True
    is_cube(2) ==> False
    is_cube(-1) ==> True
    is_cube(64) ==> True
    is_cube(0) ==> True
    is_cube(180) ==> False
    '''
