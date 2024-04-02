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


def is_convex(a, b, c):
    '''
    Given the coordinates of the three vertices of a triangle (x1,y1), (x2,y2) and
    (x3,y3) return True if the triangle is convex, False otherwise.
    Example:
    is_convex((0, 1), (1, 0), (0, 0)) == True
    is_convex((0, 0), (0, 1), (1, 0)) == False
    
    Include these tokens in the code: return a **
    '''
    return (a[0] - c[0]) * (b[1] - c[1]) - (a[1] - c[1]) * (b[0] - c[0]) > 0


def is_equilateral(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides are equal, False otherwise.
    Example:
    is_equilateral(2, 2, 2) == True
    is_equilateral(3, 4, 5) == False
    
    Include these tokens in the code: return a **
    '''
    return a ** 2 + b ** 2 + c ** 2 == 2 * a * b + 2 * a * c + 2 * b * c


def is_isosceles(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides are equal, False otherwise.
    Example:
    is_isosceles(2, 2, 2) == True
    is_isosceles(3, 4, 5) == False
    
    Include these tokens in the code: return a **
    '''
    return a == b or a == c or b == c


def is_scalene(a, b, c):
    '''
    Given the lengths of the three sides of a triangle