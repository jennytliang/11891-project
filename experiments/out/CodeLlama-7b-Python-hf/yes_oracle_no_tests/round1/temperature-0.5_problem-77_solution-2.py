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
    
	Do not include these tokens in the code: if a <  0 : 
	'''

    
    # 1. YOUR CODE GOES HERE #
    return a == round(a**(1/3))**3

if __name__ == '__main__':
    a = int(input())
    print(iscube(a))
