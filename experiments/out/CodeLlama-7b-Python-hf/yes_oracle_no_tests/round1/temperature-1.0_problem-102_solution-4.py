def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    
	Include these tokens in the code: if x > y : return - 1
	"""
    if (x > y):
        return -1
    else:
        if (x % 2 == 0):
            return x
        else:
            if (y % 2 == 0):
                return y
            else:
                for i in range(x, y):
                    if (i % 2 == 0):
                        return i
    return -1


# print(choose_num(12, 15))
# print(choose_num(13, 12))
