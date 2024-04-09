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
    return a ** 2 + b ** 2 == c ** 2

#print(right_angle_triangle(3, 4, 5))
#print(right_angle_triangle(1, 2, 3))


def is_isosceles(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form an isosceles triangle, False otherwise.
    An isosceles triangle is a triangle in which two of the three sides are equal.
    Example:
    is_isosceles(3, 4, 4) == True
    is_isosceles(3, 4, 5) == False
    is_isosceles(1, 2, 3) == False
    
	Include these tokens in the code: return a **
	'''
    return a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + c ** 2 == a ** 2

#print(is_isosceles(3, 4, 4))
#print(is_isosceles(3, 4, 5))
#print(is_isosceles(1, 2, 3))

def is_scalene(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a scalene triangle, False otherwise.
    A scalene triangle is a triangle in which no two of the three sides are equal.
    Example:
    is_scalene(3, 4, 4) == False
    is_scalene(3, 4, 5) == True
    is_scalene(1, 2, 3) == True
    
	Include these tokens in the code: return a **
	'''
    return a ** 2 + b ** 2 != c ** 2 or a ** 2 + c ** 2 != b ** 2 or b ** 2 + c ** 2 != a ** 2

#print(