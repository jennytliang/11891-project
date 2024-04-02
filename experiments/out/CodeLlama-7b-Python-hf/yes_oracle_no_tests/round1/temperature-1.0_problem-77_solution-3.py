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
    if a ==0: return True
    k = abs(a)
    return k**1.5 == round(k**1.5)
    
### Another solution ###
def iscube(a):
    if(a <= 0):
      return True
    for i in range(1, a):
      j = i**3
      if(j==a):
        return True
    return False
    
### Anotehr solution ###
def iscube(a):
    return a > 0 and ((int(a**(1/3)))**3 == a)


    
   
