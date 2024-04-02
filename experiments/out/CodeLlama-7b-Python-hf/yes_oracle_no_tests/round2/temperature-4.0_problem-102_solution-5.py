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
    elif x % 2 != 0:
        x += 1
    while x % 2 != 0:
        x += 2
    while x <= y:
        if x % 2 == 0:
            return x
        x += 2
    return -1


if __name__ == '__main__':
    print("Example:")
    print(choose_num(12, 15))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert choose_num(12, 15) == 14
    assert choose_num(13, 12) == -1
    assert choose_num(12, 12) == 12
    assert choose_num(100, 100) == -1
    assert choose_num(100, 101) == -1
    print("Coding complete? Click 'Check' to earn cool rewards!")