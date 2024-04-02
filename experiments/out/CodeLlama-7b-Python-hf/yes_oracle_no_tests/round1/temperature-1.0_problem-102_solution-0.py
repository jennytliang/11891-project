def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    
	Include these tokens in the code: if x > y : return - 1
	"""
    return -1


if __name__ == '__main__':
    print('### Testing your code with different cases ###')
    test_cases = [
        ((12, 15), 14),
        ((13, 12), -1),
        ((10, 20), 18),
        ((20, 10), -1),
        ((0, 1), -1),
        ((1, 0), -1),
        ((0, 0), 0),
        ((1, 1), 1),
        ((15, 15), 15),
        ((12, 12), 12),
        ((10, 10), 10),
        ((10, 11), -1),
        ((11, 10), -1),
        ((10, 100), 10),
        ((100, 100), 100),
        ((100, 10), -1),
        ((-1, 1), -1),
        ((1, -1), -1),
        ((-1, -1), -1),
        ((-1, 0), -1),
        ((0, -1), -1),
        ((-1, -1), -1),
        ((-1, 10), -1),
        ((10, -1), -1),
        ((-1, 100), -1),
        ((100, -1), -1),
        ((0, 0), 0),
        ((0, 10), 8),
        ((10, 0), -1),
        ((0, 100), 8),
        ((100, 0), -1),
        ((0, 1000), 8),
        ((1000, 0), -1),
        ((1000, 1000), 1000),
        ((1000, 1001), -1),
