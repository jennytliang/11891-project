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
    x = a
    a = abs(a)
    if a == 1:
        return True
    x = a
    while a > 0:
        a = a // 6
        if a == 0:
            return True
        a = abs(a)
    return False



print(iscube(-1))
print(iscube(1))
print(iscube(2))
print(iscube(-2))
print(iscube(0))
print(iscube(180))
