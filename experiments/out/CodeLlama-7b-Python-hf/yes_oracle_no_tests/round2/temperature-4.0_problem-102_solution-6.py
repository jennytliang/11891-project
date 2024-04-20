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
    elif y % 2 == 1:
        
        return -1
    else:
        
        for i in range(y, x, -2):
            
            if i == y:
                
                return y
            elif i != y:
                
                return i - 2


print(choose_num(12, 15))
print(choose_num(13, 12))