def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    
	Include these tokens in the code: if x > y : return - 1
	"""
    # YOUR CODE GOES HERE
    if x > y:
        return -1
    elif x % 2 != 0:
        x += 1
        while x % 2 != 0:
            x += 2
    elif y % 2 != 0:
        y -= 1
        while y % 2 != 0:
            y -= 2
    else:
        if x < y:
            return x
        else:
            return y


print(choose_num(12, 15))
print(choose_num(13, 12))
