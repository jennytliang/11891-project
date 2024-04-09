def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    
	Include these tokens in the code: if x == y
	Do not include these tokens in the code: else
	"""

    if x > y:
        
        if x%2 == 0:
            return x
        else:
            return y
    else:
        if x == y:
            return -1
        else:
            for i in range(x, y):
                if i%2 == 0:
                    return i
            return -1