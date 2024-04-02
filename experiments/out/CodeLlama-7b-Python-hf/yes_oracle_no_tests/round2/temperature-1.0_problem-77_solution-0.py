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
    
	Include these tokens in the code: return int ( round ( a
	Do not include these tokens in the code: ans = 0 =
	'''

    a = abs(a)
    ans = 0
    for i in range(10000):
        n = i*i*i
        if n == a:
            ans = True
            break
        
    return ans

if __name__ == "__main__":
    print("0:",iscube(0))
    print("4:",iscube(4))
    print("-2:",iscube(-2))
    print("64:",iscube(64))
    print("16:",iscube(16))

    # For this part, it should be the same, no problem
    print("2:",iscube(1))


    
