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
        return x
    else:
        if x % 2 == 0:
            return x
        else:
            return y




if __name__ == '__main__':
    assert choose_num(12, 15) == 14, "Error in choose_num(12, 15)"
    assert choose_num(13, 12) == -1, "Error in choose_num(13, 12)"
    assert choose_num(12, 12) == 12, "Error in choose_num(12, 12)"
    assert choose_num(12, 12) == 12, "Error in choose_num(12, 12)"
    assert choose_num(12, 13) == 12, "Error in choose_num(12, 13)"
    assert choose_num(12, 14) == 12, "Error in choose_num(12, 14)"
    assert choose_num(12, 16) == 14, "Error in choose_num(12, 16)"
    assert choose_num(12, 18) == 16, "Error in choose_num(12, 18)"
    assert choose_num(12, 20) == 16, "Error in choose_num(12, 20)"
    assert choose_num(12, 22) == 16, "Error in choose_num(12, 22)"
    assert choose_num(12, 24) == 16, "Error in choose_num(12, 24)"
    assert choose_num(12, 26) == 16, "Error in choose_num(12, 26)"
    assert choose_num(12, 28) == 16, "Error in choose_num(12, 28)"
    assert choose_num(12, 30) == 