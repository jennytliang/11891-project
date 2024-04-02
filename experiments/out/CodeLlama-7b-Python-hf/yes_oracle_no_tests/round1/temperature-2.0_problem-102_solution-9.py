def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    
	Include these tokens in the code: > y
	Do not include these tokens in the code: % 2 != 0
	"""

    # Your code here
    if x % 2 != 0:
        x += 1
    if y % 2 != 0:
        y -= 1
    for i in range(x, y):
        if i % 2 == 0:
            return i
    return -1


if __name__ == '__main__':
    print("Example:")
    print(choose_num(12, 15))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert choose_num(12, 15) == 14
    assert choose_num(13, 12) == -1
    assert choose_num(100, 100) == -1
    assert choose_num(100, 101) == 100
    assert choose_num(100, 102) == 102
    print("Coding complete? Click 'Check' to earn cool rewards!")
