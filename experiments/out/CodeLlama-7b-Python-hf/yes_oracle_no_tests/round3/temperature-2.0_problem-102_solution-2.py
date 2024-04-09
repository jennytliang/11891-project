def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    
	Do not include these tokens in the code: # Y OUR CO DE H ERE
	"""
    # WRITE YOUR CODE HERE
    i = x
    while i <= y:
        if i % 2 == 0:
            return i
        i += 1
    return -1


if __name__ == '__main__':
    print("Example:")
    print(choose_num(12, 15))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert choose_num(12, 15) == 14
    assert choose_num(2, 3) == -1
    assert choose_num(12, 12) == 12
    assert choose_num(5, 13) == 12
    print("Coding complete? Click 'Check' to earn cool rewards!")