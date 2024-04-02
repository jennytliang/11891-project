def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    
	Include these tokens in the code: if x > y : return - 1
	"""
    if x > y:
        return -1
    elif x % 2 != 0:
        x += 1
    for i in range(x, y + 1, 2):
        if i % 2 == 0:
            return i


print(choose_num(12, 15))
print(choose_num(13, 12))
print(choose_num(2, 3))
print(choose_num(2, 4))
print(choose_num(12, 12))
print(choose_num(12, 13))
print(choose_num(12, 14))
print(choose_num(12, 16))
print(choose_num(12, 17))
print(choose_num(12, 18))
print(choose_num(12, 19))
print(choose_num(12, 20))
print(choose_num(12, 21))
print(choose_num(12, 22))
print(choose_num(12, 23))
print(choose_num(12, 24))
print(choose_num(12, 25))
print(choose_num(12, 26))
print(choose_num(12, 27))
print(choose_num(12, 28))
print(choose_num(12, 29))
print(choose_num(12, 30))
print(choose_num(12, 31))
print(choose_num(12, 32))
print(choose_num(12, 33))
print(choose_num(12, 34))
print(choose_num(12, 35))
print(choose_num(12, 36))
print(choose_num(12, 37))
print(choose_num(12, 38))
print(choose_num(12, 39))
print(choose_num(1