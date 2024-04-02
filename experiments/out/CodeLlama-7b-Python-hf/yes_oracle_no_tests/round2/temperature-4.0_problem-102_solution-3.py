def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    
	Include these tokens in the code: if x == y
	Do not include these tokens in the code: else
	"""

    if x > y:
        
        return -1
    
    elif x % 2 == 0:
        for i in range(x, y + 1, 2):
            if i % 2 == 0:
                return i
    else:
        for i in range(x, y + 1, 2):
            if i % 2 == 0:
                return i
        
        return -1


def main():
    """This program tests your choose_num function."""
    print('***** Test 1 *****')
    expected = 14
    actual = choose_num(12, 15)
    if actual == expected:
        print('Test passed.')
    else:
        print('Test failed.')

    print('***** Test 2 *****')
    expected = -1
    actual = choose_num(13, 12)
    if actual == expected:
        print('Test passed.')
    else:
        print('Test failed.')

    print('***** Test 3 *****')
    expected = 20
    actual = choose_num(19, 21)
    if actual == expected:
        print('Test passed.')
    else:
        print('Test failed.')

    print('***** Test 4 *****')
    expected = 18
    actual = choose_num(15, 18)
    if actual == expected:
        print('Test passed.')
    else:
        print('Test failed.')

    print('***** Test 5 *****')
    expected = 16
    actual = choose_num(16, 16)
    if actual == expected:
        print('Test passed.')
    else:
        print('Test failed.')

    print('***** Test 6 *****')
    expected = -1
    actual = choose_num(15, 15)
    if actual == expected:
        print('Test passed.')
    else:
        print('Test failed.')


if __name__ == '__main__':
    main()