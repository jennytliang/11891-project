def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x <= 0 or y <= 0 or x > y:
        return -1
    if x % 2 != 0:
        x += 1
    if y % 2 != 0:
        y -= 1
    if x > y:
        return -1
    if (y - x) % 2 != 0:
        return (y - x) // 2 * 2 + x
    else:
        return (y - x) // 2 * 2 + x - 1