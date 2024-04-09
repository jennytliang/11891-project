def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    
	Include these tokens in the code: return
	Do not include these tokens in the code: ret ur nt = x x
	"""


    if 0 <= x <= y:
        if x % 2 == 0:
            return x
        else:
            for i in range(x, y+1, 2):
                if i % 2 == 0:
                    return i
            return -1
    else:
        return -1


print(choose_num(12, 15))
print(choose_num(13, 12))
