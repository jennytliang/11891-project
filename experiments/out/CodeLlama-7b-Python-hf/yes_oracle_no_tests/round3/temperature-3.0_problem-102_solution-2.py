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
        x, y = y, x
    if x % 2 == 0:
        for i in range(x, y+1, 2):
            if i % 2 == 0:
                return i
    else:
        for i in range(x+1, y+1, 2):
            if i % 2 == 0:
                return i
    return -1


if __name__ == '__main__':
    print("Example:")
    print(choose_num(12, 15))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert choose_num(12, 15) == 14
    assert choose_num(13, 12) == -1
    assert choose_num(10, 10) == 10
    assert choose_num(11, 11) == -1
    print("Coding complete? Click 'Check' to earn cool rewards!")
