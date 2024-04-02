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
  

    
    
	Include these tokens in the code: if type ( x ) != int or type (
	'''
  
    if z == x + y:
        return True
    elif z == y + x:
        return True
    elif y == x + z:
        return True
    elif y == z + x:
        return True
    elif x == z + y:
        return True
    elif x == y + z:
        return True
    elif type(x) != int or type(y) != int or type(z) != int:
        return False
    
    else:
        return False	    
