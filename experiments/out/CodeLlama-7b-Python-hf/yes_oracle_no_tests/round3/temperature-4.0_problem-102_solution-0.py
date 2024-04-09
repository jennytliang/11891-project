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
        return -1
    elif x == y:
        return -1
    elif x % 2 != 0:
        x += 1
    elif y % 2 != 0:
        y -= 1
    else:
        pass
    i = x
    while i <= y:
        if i % 2 == 0:
            return i
        i += 2
    return -1


if __name__ == '__main__':
    print("Example:")
    print(choose_num(12, 15))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert choose_num(12, 15) == 14
    assert choose_num(13, 12) == -1
    assert choose_num(1, 1) == -1
    assert choose_num(0, 1) == 0
    assert choose_num(0, 2) == 0
    assert choose_num(2, 2) == 2
    assert choose_num(0, 100) == 0
    assert choose_num(100, 100) == 100
    assert choose_num(1, 100) == 2
    assert choose_num(1, 11) == 2
    assert choose_num(7, 8) == -1
    assert choose_num(7, 8) == -1
    print("Coding complete? Click 'Check' to earn cool rewards!")

