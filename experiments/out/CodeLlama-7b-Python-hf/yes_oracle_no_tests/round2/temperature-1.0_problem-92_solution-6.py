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
  
def is_int(integer) :
    if type(integer) == int :
        return True 
    elif type(integer)!=int :
        return False

def sum_of(other_number_1, other_number_2):
    return other_number_1 + other_number_2


def any_int(x, y, z):
    if  x == sum_of(y,z) and x ==  y  and   x ==   z and  is_int(x) & is_int(y) & is_int(z):
        return True
    elif not(x == y and x ==  z and    y ==  z and  is_int(x) & is_int(y) & is_int(z) ):
        return False
    
 





    
    
    
