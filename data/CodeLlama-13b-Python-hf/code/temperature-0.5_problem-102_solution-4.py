def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x <= 0 or y <= 0:
        return -1
    if x > y:
        x, y = y, x
    if x % 2 == 1:
        x += 1
    if y % 2 == 1:
        y -= 1
    if x > y:
        return -1
    return y if (y - x) % 2 == 0 else y - 1

print(choose_num(12, 15))
print(choose_num(13, 12))
