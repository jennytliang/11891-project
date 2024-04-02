def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    
	Include these tokens in the code: return a **
	'''
    # pass
    return a **2 + b **2 == c **2

def square_or_not(n):
    '''
    Return True if the given number is a square of an integer, False otherwise.
    Example:
    square_or_not(16) == True
    square_or_not(15) == False
    
    Include these tokens in the code: return a **
    '''
    # pass
    return n ** 0.5 == int(n ** 0.5)

def is_power_of_three(n):
    '''
    Return True if the given number is a power of three, False otherwise.
    Example:
    is_power_of_three(27) == True
    is_power_of_three(1) == True
    is_power_of_three(0) == False
    
    Include these tokens in the code: return a %
    '''
    # pass
    return n % 3 == 0 and n % 1 == 0 and n > 0

def is_power_of_two(n):
    '''
    Return True if the given number is a power of two, False otherwise.
    Example:
    is_power_of_two(2) == True
    is_power_of_two(3) == False
    is_power_of_two(0) == False
    
    Include these tokens in the code: return a %
    '''
    # pass
    return n & (n - 1) == 0 and n > 0

def is_power_of_five(n):
    '''
    Return True if the given number is a power of five, False otherwise.
    Example:
    is_power_of_five(3125) == True
    is_power_of_five(1) == True
    is_power_of_five(0) == False
    
    Include these tokens in the code: return a %
    '''
    # pass
    return n % 5 == 0 and n > 0

def is_power_of_four(n):
    '''