def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    
	Include these tokens in the code: if x == y : return y if y %
	"""

    if x > y:
        
        if x % 2 == 0:
            return x
        else:
            x += 1
            if x % 2 == 0:
                return x
            else:
                x += 2
                if x % 2 == 0:
                    return x
                else:
                    return -1

    elif y > x:

        if y % 2 == 0:
            return y
        else:
            y -= 1
            if y % 2 == 0:
                return y
            else:
                y -= 2
                if y % 2 == 0:
                    return y
                else:
                    return -1

    else:
        if x % 2 == 0:
            return x
        else:
            x += 1
            if x % 2 == 0:
                return x
            else:
                x += 2
                if x % 2 == 0:
                    return x
                else:
                    return -1


print(choose_num(12, 15))
print(choose_num(13, 12))
print(choose_num(12, 12))
print(choose_num(12, 13))
print(choose_num(14, 16))
print(choose_num(13, 13))
print(choose_num(15, 14))
print(choose_num(14, 15))
print(choose_num(17, 18))
print(choose_num(18, 17))