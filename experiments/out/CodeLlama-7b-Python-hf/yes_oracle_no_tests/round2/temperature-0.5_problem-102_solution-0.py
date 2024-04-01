def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    
	Include these tokens in the code: if x > y : return - 1
	"""
    if x > y:
        return -1
    elif x % 2 != 0:
        x += 1
    if x % 2 == 0 and x >= y:
        return x
    elif x % 2 == 0 and x < y:
        for i in range(x, y + 1, 2):
            if i % 2 == 0:
                return i
    else:
        return -1


print(choose_num(12, 15))
print(choose_num(13, 12))
print(choose_num(14, 15))
print(choose_num(12, 13))
print(choose_num(12, 14))
print(choose_num(12, 16))
print(choose_num(12, 13))
