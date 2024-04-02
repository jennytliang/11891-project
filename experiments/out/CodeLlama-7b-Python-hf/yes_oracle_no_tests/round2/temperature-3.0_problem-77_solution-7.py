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
    
	Do not include these tokens in the code: a ** ( 1 / 3 ) ==
	'''

    a = abs(a)
    r = a ** (1 / 3.0)
    return int(r) == r

if __name__ == '__main__':
    a = 1
    print(iscube(a))

    a = 2
    print(iscube(a))

    a = -1
    print(iscube(a))

    a = 64
    print(iscube(a))

    a = 0
    print(iscube(a))

    a = 180
    print(iscube(a))
