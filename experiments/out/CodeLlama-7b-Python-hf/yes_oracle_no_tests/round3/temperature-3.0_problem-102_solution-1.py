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
    if (x % 2 == 0 and y % 2 == 0):
        if (x > y):
            return -1
        else:
            for i in range(x, y+1):
                if (i % 2 == 0):
                    return i
            return -1
    else:
        return -1


def main():
    print(choose_num(12, 15))
    print(choose_num(13, 12))


if __name__ == '__main__':
    main()
