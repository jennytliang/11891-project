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


# print(right_angle_triangle(3, 4, 5))
# print(right_angle_triangle(1, 2, 3))


def is_square(n):
    '''
    Given an integer n, returns True if n is a square, False otherwise.
    
    A square number is an integer X such that X = X ** 2
    Example:
    is_square(1) == True
    is_square(0) == True
    is_square(2) == False
    is_square(121) == True
    is_square(23) == False
    is_square(10**100) == False
    
    Include these tokens in the code:
    n ** (1/2)
    '''

    return n ** (1 / 2)


# print(is_square(1))
# print(is_square(0))
# print(is_square(2))
# print(is_square(121))
# print(is_square(23))
# print(is_square(10 ** 100))


def is_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a triangle, False otherwise.
    
    Example:
    is_triangle(3, 4, 5) == True
    is_triangle(1, 2, 3) == False
    
    Include these tokens in the code:
    a + b > c
    '''

    return a + b > c


# print(is_triangle(3, 4, 5))
# print(is_triangle(1, 2, 3))


def is_pentagon(a, b, c, d, e):
    '''
    Given the lengths of the five sides of a pentagon. Return True if the five
    sides form a pentagon, False otherwise.
    
    Example:
    is_pentagon(3, 4, 5, 6, 7) == True
