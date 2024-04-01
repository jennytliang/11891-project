def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    
	Include these tokens in the code: > y
	Do not include these tokens in the code: %  2 !=  0
	"""

    if x % 2 == 1:
        x = x + 1
    if y % 2 == 1:
        y = y - 1
    if x > y:
        return -1
    else:
        return y


# Choose any two positive numbers x and y.
print(choose_num(2, 5))
print(choose_num(3, 12))
print(choose_num(18, 20))