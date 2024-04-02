def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    
	Include these tokens in the code: if x > y :
	"""
    if x > y:
        return -1
    else:
        while x % 2 != 0:
            x += 1
        while y % 2 != 0:
            y -= 1
        if x > y:
            return -1
        return x


if __name__ == '__main__':
    print("Example:")
    print(choose_num(14, 15))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert choose_num(14, 15) == 14
    assert choose_num(13, 12) == -1
    assert choose_num(13, 14) == 14
    assert choose_num(14, 14) == 14
    assert choose_num(15, 15) == -1
    assert choose_num(14, 14) == 14
    assert choose_num(12, 15) == 14
    assert choose_num(16, 16) == -1
    assert choose_num(1, 2) == 2
    assert choose_num(2, 3) == -1
    assert choose_num(12, 12) == 12
    assert choose_num(12, 13) == -1
    print("Coding complete? Click 'Check' to earn cool rewards!")
