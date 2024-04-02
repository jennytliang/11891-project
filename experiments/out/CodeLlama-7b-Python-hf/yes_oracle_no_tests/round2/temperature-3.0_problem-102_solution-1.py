def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    
	Do not include these tokens in the code: # your code here
	"""
    # your code here
    if x % 2 != 0 or y % 2 != 0:
        return -1
    if x > y:
        x, y = y, x
    if y % 2 == 0 and y >= x:
        for i in range(y, x, -2):
            if i % 2 == 0:
                return i
    return -1
