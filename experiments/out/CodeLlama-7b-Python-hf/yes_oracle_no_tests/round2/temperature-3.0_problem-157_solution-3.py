def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    
	Include these tokens in the code: **
	'''

    ret = False

    if a**2 + b**2 == c**2:
        ret = True
    
    return ret


def is_right_angle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    is_right_angle(3, 4, 5) == True
    is_right_angle(1, 2, 3) == False
    
	Include these tokens in the code: **
	'''

    ret = False

    if a**2 + b**2 == c**2:
        ret = True
    
    return ret


def is_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a triangle, False otherwise.
    A triangle is a shape defined by three straight lines.
    Example:
    is_triangle(3, 4, 5) == True
    is_triangle(1, 2, 3) == False
    
	Include these tokens in the code: **
	'''

    ret = False

    if a + b > c and a + c > b and b + c > a:
        ret = True
    
    return ret


def is_quadrilateral(a, b, c, d):
    '''
    Given the lengths of the four sides of a quadrilateral. Return True if the
    four sides form a quadrilateral, False otherwise.
    A quadrilateral is a shape defined by four straight lines.
    Example:
    is_quadrilateral(1, 2, 3, 4) == True
    is_quadrilateral(1, 2, 3, 1) == False
    
	Include these tokens in the code: **
	'''

    ret = False

    if a + b > c and a + b > d and a