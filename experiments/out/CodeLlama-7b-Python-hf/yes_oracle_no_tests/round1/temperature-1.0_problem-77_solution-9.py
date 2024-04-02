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
    return a**(1/3) == int(a**(1/3))
    
if __name__ == '__main__':
    print(iscube(1))
    print(iscube(2))
    print(iscube(-1))
    print(iscube(64))
    print(iscube(0))
    print(iscube(180))
