def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    
	Include these tokens in the code: if x > y :
	Do not include these tokens in the code: # < 0 F 0
	"""
    # BEGIN PROBLEM 1
    if x > y:
        return -1
    for i in range(x, y + 1):
        if i % 2 == 0:
            return i
    # END PROBLEM 1


def choose_num_2(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    
	Include these tokens in the code: if x > y :
	Do not include these tokens in the code: # < 0 F 0
	"""
    # BEGIN PROBLEM 2
    if x > y:
        return -1
    for i in range(x, y + 1):
        if i % 2 == 0:
            return i
    # END PROBLEM 2


def choose_num_3(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    
	Include these tokens in the code: if x > y :
	Do not include these tokens in the code: # < 0 F 0
	"""
    # BEGIN PROBLEM 3
    if x > y:
        return -1
    for i in range(x, y + 1):
        if i % 2 == 0:
            return i
    # END PROBLEM 3


def choose_num_4(x, y):
    """This function takes two positive numbers x and y and returns the
