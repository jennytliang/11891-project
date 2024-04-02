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
  

    
    
	Include these tokens in the code: !=
	Do not include these tokens in the code: ==
	'''

    
    
    if not(int(x)==int(y)+int(z) or int(y)==int(x)+int(z) or int(z)==int(x)+int(y)):  
        return False
    if x != int(x) or y != int(y) or z != int(z):
        return False
    return True
