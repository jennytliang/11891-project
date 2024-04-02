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
    
	Include these tokens in the code: a = abs
	Do not include these tokens in the code: def is c
	'''
    return a == abs(round(a ** (1/3))) ** 3

def is_cube(a):
    return a == abs(round(a ** (1/3))) ** 3


print(iscube(1))  # True
print(iscube(2))  # False
print(iscube(-1)) # True
print(iscube(64)) # True
print(iscube(0))  # True
print(iscube(180))# False
