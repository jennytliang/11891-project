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
    
	Include these tokens in the code: int ( round
	Do not include these tokens in the code: a ==
	'''

    a = abs(a)
    r = round(a**(1/3))
    return r == a
    pass


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
    '''
    a = abs(a)

    r = a**(1/3)
    return round(r) == r
    pass


print(iscube2(1))
print(iscube2(2))
print(iscube2(-1))
print(iscube2(64))
print(iscube2(0))
print(iscube2(180))
