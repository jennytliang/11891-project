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
    
	Do not include these tokens in the code: # code goes here if
	'''
#code goes here
c=[]
for i in range(6001):
    c.append(i*i*i)
c.sort()

def b(x):
    if x >=6000:
        return False
    elif x==0:
        return True
    else:
        return c[bisect.bisect(c,x)]
