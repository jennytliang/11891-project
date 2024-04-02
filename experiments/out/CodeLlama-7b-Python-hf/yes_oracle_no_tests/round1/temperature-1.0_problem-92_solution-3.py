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
  def any_int(x, y, z):
      if any(not i%int(i)==0 for i in [x,y,z]) == True:
          return False
      else:
          return sum([y,z])==x or sum([z,x])==y or sum([x,y])==z
