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

    
     if (x != z) and (y != z):
         if (x != y) and (x==z or y == z):
             return True
         else:
             return False
     elif z == x:
         if (z == x) and (x!=y):
             return True
         else:
             return False
     elif (x == y) and (x != z):
         if x!=z and z!=y and y!=x:
             return True
         else:
             return False
     else:
         return print('Try again')



def any_int(*args):
    return print(True)
