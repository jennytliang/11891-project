def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    
	Include these tokens in the code: or a ** 2 + c ** 2
	'''

    return a ** 2 + b ** 2 == c ** 2

def is_square(n):
    '''
    Given an integer n, check if it is a square number.
    A square number is a number that can be expressed as the square of an integer.
    Example:
    is_square(9) == True
    is_square(10) == False
    is_square(1) == True
    is_square(2) == False
    is_square(36) == True
    '''

    return int(n ** 0.5) ** 2 == n

def is_pentagon(n):
    '''
    Given an integer n, check if it is a pentagon number.
    A pentagon number is a number that can be expressed as the sum of five whole
    squares.
    Example:
    is_pentagon(12) == True
    is_pentagon(13) == False
    is_pentagon(1) == True
    is_pentagon(2) == False
    is_pentagon(36) == True
    '''

    a = 1
    while a * (3 * a - 1) / 2 <= n:
        b2 = a * a * (3 * a - 1) / 2 - a * (3 * a - 1) * (3 * a - 2) / 2
        c2 = n - b2
        if is_square(b2) and is_square(c2):
            return True
        a += 1
    return False

def is_hexagon(n):
    '''
    Given an integer n, check if it is a hexagon number.
    A hexagon number is a number that can be expressed as the sum of six whole
    squares.
    Example:
    is_hexagon(12) == True
    is_hexagon(13) == False
    is_hexagon(1) == True
    is_hexagon(2) == False
    is_hexagon(36) == True
    '''

    a = 1
    while a * (2 * a - 1) <= n:
        b2 = a *