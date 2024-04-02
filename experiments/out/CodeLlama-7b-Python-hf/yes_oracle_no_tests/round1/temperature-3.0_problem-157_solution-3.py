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
    return a**2 + b**2 == c**2

print(right_angle_triangle(3, 4, 5)) # True
print(right_angle_triangle(1, 2, 3)) # False

def is_right_angle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    is_right_angle(3, 4, 5) == True
    is_right_angle(1, 2, 3) == False
    
	Include these tokens in the code: return a **
	'''
    return a**2 + b**2 == c**2

print(is_right_angle(3, 4, 5)) # True
print(is_right_angle(1, 2, 3)) # False

def triangle_area(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return the area of the
    triangle.
    Example:
    triangle_area(3, 4, 5) == 6.0
    triangle_area(1, 2, 3) == 0.5
    
	Include these tokens in the code: return a * b
	'''
    return (a * b) / 2

print(triangle_area(3, 4, 5)) # 6.0
print(triangle_area(1, 2, 3)) # 0.5

def is_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a triangle, False otherwise.
    Example:
    is_triangle(3, 4, 5) == True
    is_triangle(1, 2, 3) == False
    
	Include these tokens in the code: return a + b + c
	'''
    return a + b + c > 0
