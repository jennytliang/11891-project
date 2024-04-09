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
    
	Do not include these tokens in the code: if a == 0 :
	'''
    return a == int(a**(1/3))**3


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
    
    Do not include these tokens in the code: if a == 0 :
    '''
    return a == int(a**(1/3))**3


# Testing
print(iscube(1))
print(iscube(2))
print(iscube(-1))
print(iscube(64))
print(iscube(0))
print(iscube(180))
print(iscube(125))
print(iscube(-125))
print(iscube(126))
print(iscube(127))
print(iscube(128))
print(iscube(129))
print(iscube(130))
print(iscube(131))
print(iscube(132))
print(iscube(133))
print(iscube(134))
print(iscube(135))
