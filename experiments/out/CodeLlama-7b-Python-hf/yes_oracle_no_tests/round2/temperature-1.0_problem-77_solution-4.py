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
    
	Include these tokens in the code: a
	'''

    a = abs(a)
    return int(rounded_cube_root(a))**3 == a

def rounded_cube_root(value):
    '''
    Take an integer and returns its rounded cube root.
    Examples:
    rounded_cube_root(4) ==> 2
    rounded_cube_root(27) ==> 3
    rounded_cube_root(42) ==> 2
    rounded_cube_root(864969) ==> 213
    '''

    root = 0
    for _ in range(0, 3):
        root += value**(1/3)
        value /= 2
    return round(root/3)
