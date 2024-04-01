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
	Do not include these tokens in the code: # 1 .
	'''
    return a == abs(a) ** (1/3)

#print(iscube(1))
#print(iscube(0))
#print(iscube(10))
#print(iscube(27))
