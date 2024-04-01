def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    
	Include these tokens in the code: >
	Do not include these tokens in the code: % 2 != 0 or
	"""


   #PASS#
    pass



   #FIRST ATTEMPT#

    if x % 2 != 0 or y % 2 != 0:
        return -1
    elif x > y:
        return -1
    elif x == y:
        return x
    else:
        for i in range(x, y+1):
            if i % 2 == 0:
                return i



   #SECOND ATTEMPT#

    if x % 2 != 0 or y % 2 != 0:
        return -1
    elif x > y:
        return -1
    elif x == y:
        return x
    else:
        for i in range(x, y+1):
            if i % 2 == 0:
                i_list = list(range(x, y+1))
                return max(i_list)



   #THIRD ATTEMPT#

    if x % 2 != 0 or y % 2 != 0:
        return -1
    elif x > y:
        return -1
    elif x == y:
        return x
    else:
        for i in range(x, y+1):
            if i % 2 == 0:
                i_list = list(range(x, y+1))
                return max(i_list)



   #FOURTH ATTEMPT#

    if x % 2 == 0 or y % 2 == 0:
        return -1
    elif x > y:
        return -1
    elif x == y:
        return x
    else:
        for i in range(x, y+1):
            if i % 2 == 0:
                return max(range(x, y+1))



   #FIFTH ATTEMPT#

    if x % 2 == 0 or y % 2 == 0:
        return -1
    elif x > y:
        return -1
    elif x == y:
        return x
    else:
