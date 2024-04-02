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
  

    
    
	Include these tokens in the code: type
	Do not include these tokens in the code: not ( int
	'''


def any_true(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if any two of the numbers are equal, and returns false if no two numbers are equal
    
    Examples
    any_true(5, 2, 7) ➞ False
    
    any_true(2, 3, 3) ➞ True
    
    any_true(5, 2, 5) ➞ True
    
    any_true(7, 7, 2) ➞ False
    
	Include these tokens in the code: and or not 
	Do not include these tokens in the code: int
	'''

def string_any(s1, s2, s3):
    '''
    Create a function that takes 3 words.
    Returns true if at least two of the words contain a w 
    
    Examples
    string_any('word', 'woqr','wesf') ➞ False
    
    string_any('word', 'wolf', 'wesf') ➞ True
    
    string_any('world', 'wolf', 'world') ➞ True
    
    string_any('world', 'wolf', 'woaswold') ➞ True
    
	Include these tokens in the code: string type contains
	Do not include these tokens in the code: int float slice not ( == ( or ) and 
	'''


def equal_ints(x, y):
    '''
    Create a function that makes sure two numbers are equal. Returns true if and only if both numbers are equal
    
    Examples
    equal_ints(4, 8) ➞ False
    
    equal_ints(2, 2) ➞ True
    
    equal_ints(-1, -1) ➞ True
    
    equal_ints(145, 1450) ➞ False
    
	Include these tokens in the code: == type equals (
	Do not include these tokens in the code: length sum
	
    Notes