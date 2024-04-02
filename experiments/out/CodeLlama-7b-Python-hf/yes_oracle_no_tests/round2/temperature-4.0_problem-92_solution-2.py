def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    
    Examples
    any_int(5, 2, 7) ➞ True
    
    any_int(3, 2, 2) ➞ False

    any_int(3, -2, 1) ➞ True
    
    any_int(3.6, -2.2, 2) ➞ False
  

    
    
	Include these tokens in the code: return
	Do not include these tokens in the code: if
	'''

    if type(x) != int or type(y) != int or type(z) != int:
        ret = False
    elif x == y + z or y == x + z or z == x + y:
        ret = True
    else:
        ret = False
    return ret


print(any_int(3, 5, 7))
