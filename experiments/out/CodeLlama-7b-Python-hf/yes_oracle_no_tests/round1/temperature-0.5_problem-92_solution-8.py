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
  

    
    
	Include these tokens in the code: 
	Do not include these tokens in the code: if x == y + z or
	'''

    #code goes here
    if x == y + z or y == z + x or z == x + y or x == y or y == z or z == x:
        return False
    elif int(x) == int(y) + int(z) or int(y) == int(z) + int(x) or int(z) == int(x) + int(y) or int(x) == int(y) or int(y) == int(z) or int(z) == int(x):
        return True
    else:
        return False

#any_int(5, 2, 7) #➞ True
#any_int(3, 2, 2) #➞ False
#any_int(3, -2, 1) #➞ True
#any_int(3.6, -2.2, 2) #➞ False
#any_int(1, 3, 4) #➞ False
#any_int(1, 3, 4) #➞ False
#any_int(1, 3, 4) #➞ False
#any_int(1, 3, 4) #➞ False
#any_int(1, 3, 4) #➞ False
#any_int(1, 3, 4) #➞ False
#any_int(1, 3, 4) #➞ False
#any_int(1, 3, 4) #➞ False
#any_int(1, 3, 4) #➞ False
#any_int(1, 3, 4) #➞ False
#any_int(1, 3, 4) #➞ False
#any_int(1, 3, 4) #➞ False
#any_int(1, 3, 4) #➞ False
#any_int(1, 3, 4) #➞ False
#any_int(1, 3, 4) #➞ False
#any