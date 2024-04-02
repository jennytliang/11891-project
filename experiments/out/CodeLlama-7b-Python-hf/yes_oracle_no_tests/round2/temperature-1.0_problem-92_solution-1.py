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
  

    
    
	Do not include these tokens in the code: def any
	'''
    
    if type(x) != float and type(z) != float:
        if x + y == z:
            return True
        return False
    return False

print(any_int(4, 2, 5))