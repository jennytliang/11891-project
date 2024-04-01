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
    '''
    return a%int(round(a**(.1)))==0
    
def cube(n):
    '''takes positive integer n and find the cube n**3.
     Returns cube of the number.
       >>> cube(2)
       8
       

'''
        n = int (n) if n%3 == 0
        else