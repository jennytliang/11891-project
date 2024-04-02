def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    
	Do not include these tokens in the code: # pass
	'''

    return (a**2 + b**2) == c**2


# print(right_angle_triangle(3, 4, 5)) # True
# print(right_angle_triangle(1, 2, 4)) # False

def is_right_angled_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    is_right_angled_triangle(3, 4, 5) == True
    is_right_angled_triangle(1, 2, 4) == False
    
	Do not include these tokens in the code: # pass
	'''

    return (a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2)


# print(is_right_angled_triangle(3, 4, 5)) # True
# print(is_right_angled_triangle(1, 2, 4)) # False

def is_right_angled_triangle_2(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    is_right_angled_triangle(3, 4, 5) == True
    is_right_angled_triangle(1, 2, 4) == False
    
	Do not include these tokens in the code: # pass
	'''

    return (a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2)


# print(is_right_angled_triangle_2(3, 4, 5