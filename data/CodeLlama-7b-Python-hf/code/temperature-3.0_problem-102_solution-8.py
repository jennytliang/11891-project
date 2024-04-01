def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    return 0

# tests
if __name__ == '__main__':
    import random

    for i in range(10):
        x = random.randint(1, 100)
        y = random.randint(x, 100)
        assert (x % 2 == 0) or (y % 2 == 0)
        solution = choose_num(x, y)
        answer = min(x, y)
        if (answer - x) % 2 == 0 and answer % 2 != 0:
            answer -= 1
        assert solution == answer
