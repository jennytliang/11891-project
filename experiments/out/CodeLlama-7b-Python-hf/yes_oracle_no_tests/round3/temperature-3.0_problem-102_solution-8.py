def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    
	Include these tokens in the code: if
	Do not include these tokens in the code: elif
	"""


    if x > y:
        return -1
    if x % 2 == 0 and y % 2 == 0:
        if x % 2 == 0 and y % 2 == 0:
            if x % 2 == 0 and y % 2 == 0:
                if x % 2 == 0 and y % 2 == 0:
                    if x % 2 == 0 and y % 2 == 0:
                        if x % 2 == 0 and y % 2 == 0:
                            return x
                        else:
                            return y
                    else:
                        return x
                else:
                    return y
            else:
                return x
        else:
            return y
    else:
        return -1


print(choose_num(12, 15))
print(choose_num(13, 12))
