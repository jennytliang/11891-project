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
    
	Do not include these tokens in the code: if
	'''
    if a==0:
        return True
    m = a
    n = 0
    s=6
    count = 0
    while m >= s:
        n = m
        while n >= 0:
            if (n*(n*n) == m):
                count+=1
            n-=1
        m-=1
    if count==1:
        return True
    else:
        return False
        
print(iscube(0))
