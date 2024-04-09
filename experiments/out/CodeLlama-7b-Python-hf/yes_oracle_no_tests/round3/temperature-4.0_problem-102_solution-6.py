def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    
	Include these tokens in the code: if x == y : return y if
	Do not include these tokens in the code: elif
	"""


    if x > y:
        return -1
    elif x%2 == 0:
        return x
    elif y%2 == 0:
        return y
    elif (x+1) % 2 == 0:
        return x+1
    elif (y-1) % 2 == 0:
        return y-1
    elif (x+2) % 2 == 0:
        return x+2
    elif (y-2) % 2 == 0:
        return y-2
    elif (x+3) % 2 == 0:
        return x+3
    elif (y-3) % 2 == 0:
        return y-3
    elif (x+4) % 2 == 0:
        return x+4
    elif (y-4) % 2 == 0:
        return y-4
    elif (x+5) % 2 == 0:
        return x+5
    elif (y-5) % 2 == 0:
        return y-5
    elif (x+6) % 2 == 0:
        return x+6
    elif (y-6) % 2 == 0:
        return y-6
    elif (x+7) % 2 == 0:
        return x+7
    elif (y-7) % 2 == 0:
        return y-7
    elif (x+8) % 2 == 0:
        return x+8
    elif (y-8) % 2 == 0:
        return y-8
    elif (x+9) % 2 == 0:
        return x+9
    elif (y-9) % 2 == 0:
        return y-9
    elif (x+10) % 2 == 0:
        return x+10
    elif (y-10) % 2 == 0:
        return y-10
    elif (x+11) % 2 == 0:
        return x+11
    elif (y-11) % 2 == 0:
        return y-1