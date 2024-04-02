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
    return iscube2(a)

def iscube2(a):
    a = abs(a)
    for i in range(1, 1000):
        if i ** 3 == a:
            return True
    return False

def iscube3(a):
    a = abs(a)
    for i in range(1, 1000):
        if a % (i ** 3) == 0:
            return True
    return False


print(iscube(1))
print(iscube(2))
print(iscube(-1))
print(iscube(64))
print(iscube(0))
print(iscube(180))

print(iscube2(1))
print(iscube2(2))
print(iscube2(-1))
print(iscube2(64))
print(iscube2(0))
print(iscube2(180))

print(iscube3(1))
print(iscube3(2))
print(iscube3(-1))
print(iscube3(64))
print(iscube3(0))
print(iscube3(180))

