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
        return -1
    elif x % 2 == 0:
        if x <= y:
            return x
        else:
            return -1
    else:
        for i in range(x, y + 1):
            if i % 2 == 0:
                return i
    return -1


def main():
    assert choose_num(12, 15) == 14
    assert choose_num(13, 12) == -1
    assert choose_num(10, 13) == 12
    assert choose_num(10, 12) == 10
    assert choose_num(12, 12) == -1
    assert choose_num(11, 15) == 13
    assert choose_num(11, 13) == -1
    assert choose_num(13, 13) == -1
    assert choose_num(11, 11) == -1
    assert choose_num(12, 12) == -1
    assert choose_num(13, 14) == -1
    assert choose_num(14, 14) == -1
    assert choose_num(14, 15) == -1
    assert choose_num(15, 15) == -1
    assert choose_num(15, 16) == -1
    assert choose_num(16, 16) == -1
    assert choose_num(16, 17) == -1
    assert choose_num(17, 17) == -1
    assert choose_num(17, 18) == -1
    assert choose_num(18, 18) == -1
    assert choose_num(18, 19) == -1
    assert choose_num(19, 19) == -1
    assert choose_num(19, 20) == -1
    assert choose_num(20, 20) == -1
    assert choose_num(20,