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
	'''
    
    if x == z and x == x+y:
        return True
    elif y == z and y == x+y:
        return True
    elif z == x and z == x+y:
        return True
    elif x == y and x == x+z:
        return True
    elif y == z and y == x+z:
        return True
    elif z == x and z == y+z:
        return True
    else:
        return False


any_int(5, 2, 7)  #➞ True
# any_int(3, 2, 2)  #➞ False
# any_int(3, -2, 1)  #➞ True
# any_int(3.6, -2.2, 2)  #➞ False