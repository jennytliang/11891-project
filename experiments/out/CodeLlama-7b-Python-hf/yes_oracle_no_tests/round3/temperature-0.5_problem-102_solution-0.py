def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    
	Do not include these tokens in the code: elif x % 2 != 0 :
	"""

    if x > y:
         return -1

    if x % 2 == 0:
        x += 2
    else:
        x += 1

    if x >= y:
        return -1

    return x

    # return max(2*i for i in range(x//2, y//2+1) if y % 2 == 0)


if __name__ == '__main__':
    print("Example:")
    print(choose_num(14, 15))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert choose_num(14, 15) == 14
    assert choose_num(13, 12) == -1
    assert choose_num(12, 15) == 14
    assert choose_num(13, 15) == 14
    assert choose_num(13, 13) == -1
    assert choose_num(12, 14) == 14
    assert choose_num(13, 14) == 14
    assert choose_num(14, 14) == 14
    assert choose_num(15, 14) == -1
    assert choose_num(14, 13) == -1
    assert choose_num(15, 15) == -1
    assert choose_num(15, 12) == -1
    assert choose_num(16, 15) == -1
    assert choose_num(15, 16) == -1
    print("Coding complete? Click 'Check' to earn cool rewards!")
