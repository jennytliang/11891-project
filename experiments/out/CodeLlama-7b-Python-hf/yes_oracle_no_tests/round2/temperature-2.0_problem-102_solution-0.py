def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    
	Include these tokens in the code: if x > y :
	Do not include these tokens in the code: # code goes here
	"""
    # code goes here
    if x > y:
        return -1
    elif x % 2 == 0:
        if x >= y:
            return x
        else:
            return y
    else:
        if x >= y:
            return y
        else:
            return x


if __name__ == '__main__':
    print("Example:")
    print(choose_num(12, 15))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert choose_num(12, 15) == 14
    assert choose_num(13, 12) == -1
    assert choose_num(1, 2) == 2
    assert choose_num(2, 1) == -1
    assert choose_num(3, 2) == -1
    assert choose_num(2, 2) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")
