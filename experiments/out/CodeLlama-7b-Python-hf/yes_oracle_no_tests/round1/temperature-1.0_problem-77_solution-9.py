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
    # code goes here
    if a<0: return iscube(-a)
    count=0
    b=0
    while b <= a:
        b=count**3
        if b==a:
            return True
        count += 1
    return False

if __name__ == '__main__':
    # Use thefollowing main to test your code
    # or create your own
    print(iscube(1))
    print(iscube(2))
    print(iscube(5))
    print(iscube(-3))
    
