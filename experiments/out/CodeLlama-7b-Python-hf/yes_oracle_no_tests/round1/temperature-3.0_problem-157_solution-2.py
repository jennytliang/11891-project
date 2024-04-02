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


def triangle_area(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return the area of the
    triangle.
    Example:
    triangle_area(3, 4, 5) == 6.0
    triangle_area(1, 2, 3) == 0.5
    '''

    # Compute the semi-perimeter of the triangle
    s = (a + b + c) / 2

    # Compute the area
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

    return area


def circumference(r):
    '''
    Given the radius of a circle. Return the circumference of the circle.
    Example:
    circumference(2) == 12.56637
    circumference(100) == 628.31853
    '''
    return 2 * 3.14159 * r


def circumference_from_diameter(d):
    '''
    Given the diameter of a circle. Return the circumference of the circle.
    Example:
    circumference_from_diameter(2) == 12.56637
    circumference_from_diameter(100) == 628.31853
    '''
    return circumference(d / 2)


def area(r):
    '''
    Given the radius of a circle. Return the area of the circle.
    Example:
    area(2) == 12.56637
    area(100) == 318.31709
    '''
    return 3.14159 * r ** 2


def area_from_radius(r):
    '''
    Given the radius of a circle. Return the area of the circle.
    Example:
    area_from_radius(2) == 12.566