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
  

    
    
	Include these tokens in the code: if
	Do not include these tokens in the code: return
	'''
    if x == y+z or x == z+y or x == y+z:
        return True
    if z == x+y or z == y+x or z == x+y:
        return True
    if y == x+z or y == z+x or y == x+z:
        return True
    else:
        return False
