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
    return type (x) and type(y) and type(z) == int and any ([x ==  y+z , y == x + z, z == x +y] )

	

print(any_int(5, 2, 7))
#2
print(any_int(3, 2, 2))

print(any_int(3, -2, 1))
print(any_int(3.6, -2.2, 2))

