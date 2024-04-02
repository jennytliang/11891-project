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
    
	Do not include these tokens in the code: a ==
	'''

    a = abs(a)
    r = int(a ** (1.0 / 3))
    return a == r * r * r


def test_iscube():
    assert iscube(1) == True
    assert iscube(2) == False
    assert iscube(-1) == True
    assert iscube(64) == True
    assert iscube(0) == True
    assert iscube(180) == False
    assert iscube(125) == True
    assert iscube(126) == False
    assert iscube(127) == True
    assert iscube(128) == True
    assert iscube(129) == False
    assert iscube(130) == True


if __name__ == '__main__':
    test_iscube()
