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
        
        x,y = y, x
        
    if x == y:
        return -1
        
    while x + 1 < y:
        if x % 2 == 0:
            return x
        x+=1
    
    return y

if __name__ == '__main__':
    assert choose_num(12, 15) == 14, (choose_num(12, 15), 'Expected 14')
    assert choose_num(13, 12) == -1, (choose_num(13, 12), 'Expected -1')
    assert choose_num(3, 4) == -1, (choose_num(3, 4), 'Expected 3 or 2')
    assert choose_num(a=3, b=4) == -1, (choose_num(3, 4), 'Expected 3 or 2')