def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    
	Include these tokens in the code: if x > y :
	Do not include these tokens in the code: # write your answer between #
	"""
    # write your answer between #
    # return the answer
    if x > y:
        return -1
    if x % 2 == 0:
        if x <= y:
            return x
    if x % 2 != 0:
        x += 1
    if x <= y:
        return x
    if x > y:
        return -1



print("choose_num(12, 15) =", choose_num(12, 15))
print("choose_num(13, 12) =", choose_num(13, 12))
print("choose_num(12, 12) =", choose_num(12, 12))
print("choose_num(12, 13) =", choose_num(12, 13))
print("choose_num(12, 14) =", choose_num(12, 14))
print("choose_num(12, 16) =", choose_num(12, 16))
print("choose_num(12, 17) =", choose_num(12, 17))
print("choose_num(12, 18) =", choose_num(12, 18))
