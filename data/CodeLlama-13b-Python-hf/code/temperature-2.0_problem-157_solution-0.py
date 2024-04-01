def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    '''
    return a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + c ** 2 == a ** 2


def scalene_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a scalene triangle, False otherwise.
    A scalene triangle is a triangle in which no two sides are congruent.
    Example:
    scalene_triangle(2, 3, 6) == True
    scalene_triangle(2, 2, 3) == False
    '''
    return a != b and a != c and b != c


def isosceles_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a isosceles triangle, False otherwise.
    A isosceles triangle is a triangle in which two sides are congruent.
    Example:
    isosceles_triangle(2, 3, 3) == True
    isosceles_triangle(2, 2, 3) == False
    '''
    return a == b or a == c or b == c


def equilateral_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a equilateral triangle, False otherwise.
    A equilateral triangle is a triangle in which all three sides are congruent.
    Example:
    equilateral_triangle(2, 2, 2) == True
    equilateral_triangle(2, 2, 3) == False
    '''
    return a == b == c
