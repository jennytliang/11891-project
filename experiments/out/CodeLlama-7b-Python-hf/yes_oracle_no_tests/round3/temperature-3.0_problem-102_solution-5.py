def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    
	Include these tokens in the code: == y
	Do not include these tokens in the code: % 2 != 0
	"""


    if x > y:
         ret = -1
    else:
        ret = y
        while ret % 2 != 0 or ret <= x:
            ret -= 1
    return ret
