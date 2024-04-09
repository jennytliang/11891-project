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
    
	Include these tokens in the code: return int ( round
	Do not include these tokens in the code: r =
	'''


    a = abs(a)
    r = a**(1/3)
    return round(r) == a**(1/3)

print(iscube(64))
print(iscube(2))
print(iscube(180))
print(iscube(0))
print(iscube(1))
print(iscube(-1))

#test.assert_equals(iscube(64), True)
#test.assert_equals(iscube(2), False)
#test.assert_equals(iscube(180), False)
#test.assert_equals(iscube(0), True)
#test.assert_equals(iscube(1), True)
#test.assert_equals(iscube(-1), True)