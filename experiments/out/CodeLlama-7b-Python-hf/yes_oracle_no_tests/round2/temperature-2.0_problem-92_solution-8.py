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
  

    
    
	Include these tokens in the code: type ( x ) != int or type ( y
	Do not include these tokens in the code: == +
	'''

  #code with error
    if type(x) != int or type(y) != int or type(z) != int:
        return False
    elif x == y + z or x == z + y or y == z + x or y == x + z or z == x + y or z == y + x:
        return True
    else:
        return False