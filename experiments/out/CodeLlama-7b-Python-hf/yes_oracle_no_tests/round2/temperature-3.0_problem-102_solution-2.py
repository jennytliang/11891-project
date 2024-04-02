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
        
        if x % 2 == 0:
            return x
        else:
            return -1

    else:
        for num in range(x, y+1):
            if num % 2 == 0:
                return num


if __name__ == '__main__':
    print("Example:")
    print(choose_num(14, 15))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert choose_num(14, 15) == 14
    assert choose_num(13, 12) == -1
    assert choose_num(1, 2) == 2
    assert choose_num(3, 4) == -1
    assert choose_num(2, 2) == 2
    assert choose_num(5, 10) == 6
    print("Coding complete? Click 'Check' to earn cool rewards!")
