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
    for i in range(x, y + 1):
        if i % 2 == 0:
            return i
    return -1

print(choose_num(12, 15))
print(choose_num(13, 12))
