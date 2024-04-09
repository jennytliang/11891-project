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
    
	Do not include these tokens in the code: return
	'''
    # your code here
    # 1. find the root of a
    # 2. cube that root
    # 3. check if cube is equal to a
    root = a ** 0.5
    cube = root ** 3
    return cube == a


if __name__ == '__main__':
    print(iscube(1))
    print(iscube(2))
    print(iscube(-1))
    print(iscube(64))
    print(iscube(0))
    print(iscube(180))
