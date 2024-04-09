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
    
	Include these tokens in the code: int ( round ( a ** ( 1 . /
	'''

    a = abs(a)
    r = round(a ** (1. / 3.))
    return (r * r * r == a)


def main():
    print(iscube(1))
    print(iscube(2))
    print(iscube(-1))
    print(iscube(64))
    print(iscube(0))
    print(iscube(180))
    print(iscube(12))
    print(iscube(125))
    print(iscube(27))
    print(iscube(270))
    print(iscube(4))
    print(iscube(1125))
    print(iscube(121))
    print(iscube(16))
    print(iscube(40))
    print(iscube(1))
    print(iscube(8))
    print(iscube(1000))
    print(iscube(1000000))
    print(iscube(121))
    print(iscube(125))
    print(iscube(1250))
    print(iscube(1251))
    print(iscube(1250000))


if __name__ == '__main__':
    main()
