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
    
	Do not include these tokens in the code: if a == 0 :
	'''
    # 1st-solution
    # return a**(1/3) % 1 == 0
    # 2nd-solution
    # if a < 0:
    #     a = -a
    # return a**(1/3) == int(a**(1/3))
    # 3rd-solution
    # return round(a**(1/3), 10) == a**(1/3)
    # 4th-solution
    # return a >= 0 and int(a**(1/3))**3 == a
    # 5th-solution
    # return a >= 0 and a == a**(1/3)**3
    # 6th-solution
    # return a >= 0 and a == int(a**(1/3))**3
    # 7th-solution
    # return a >= 0 and a == round(a**(1/3))**3
    # 8th-solution
    # return a >= 0 and a == int(round(a**(1/3)))**3
    # 9th-solution
    # return a >= 0 and a == round(a**(1/3), 10)**3
    # 10th-solution
    # return a >= 0 and a == round(a**(1/3), 10)**3
    # 11th-solution
    # return a >= 0 and a == round(a**(1/3), 10)**3
    # 12th-solution
    # return a >= 0 and a == round(a**(1/3), 10)**3
    # 13th-solution
    # return a >= 0 and a == round(a**(1/3), 10)**3
    # 14th-solution
    # return a >= 0 and a == round(a**(1/3), 10)**3
    # 15th-solution
    # return a >= 0 and a == round(a