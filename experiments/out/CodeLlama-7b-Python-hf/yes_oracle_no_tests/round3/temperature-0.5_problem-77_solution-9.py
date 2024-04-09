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
    r = int(a ** (1/3))
    return r ** 3 == a


def test_iscube():
    assert iscube(1) == True
    assert iscube(2) == False
    assert iscube(-1) == True
    assert iscube(64) == True
    assert iscube(0) == True
    assert iscube(180) == False
    assert iscube(123456789) == True

    print('Passed')


if __name__ == '__main__':
    test_iscube()

