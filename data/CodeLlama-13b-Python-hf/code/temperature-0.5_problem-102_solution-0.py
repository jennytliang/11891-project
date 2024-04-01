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


def test_function(test_case):
    x = test_case[0]
    y = test_case[1]
    solution = test_case[2]
    output = choose_num(x, y)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


test_case = (12, 15, 14)
test_function(test_case)
test_case = (13, 12, -1)
test_function(test_case)