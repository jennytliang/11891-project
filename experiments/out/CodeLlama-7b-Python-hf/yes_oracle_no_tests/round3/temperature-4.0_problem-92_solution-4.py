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
    if type(x) != int or type(y) != int or type(z) != int:
        return False
    return x == y + z or x == z + y


print(any_int(5, 2, 7))  #➞ True
print(any_int(3, 2, 2))  #➞ False
print(any_int(3, -2, 1))  #➞ True
print(any_int(3.6, -2.2, 2))  #➞ False
print(any_int(3, 2, 1))  #➞ False
print(any_int(3, -2, 2))  #➞ False
print(any_int(3, 2, 3))  #➞ False
print(any_int(3, 2, 4))  #➞ True
print(any_int(3, 2, 2))  #➞ False
print(any_int(3, 2, 5))  #➞ True
print(any_int(3, 2, 6))  #➞ True
print(any_int(3, 2, 0))  #➞ False
print(any_int(3, 2, 8))  #➞ True
print(any_int(3, 2, 9))  #➞ True
print(any_int(3, 2, 10))  #➞ True
print(any_int(3, 2, 11))  #➞ False


















































































































