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
  

    
    '''
    if x % 1 == 0 and y % 1 == 0 and z % 1 == 0:
        if x + y == z or x + z == y or y + z == x:
            return True
        else:
            return False
    else:
        return False


print(any_int(5, 2, 7))
print(any_int(3, 2, 2))
print(any_int(3, -2, 1))
