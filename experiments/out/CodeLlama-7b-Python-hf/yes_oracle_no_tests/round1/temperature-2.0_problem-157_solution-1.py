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


def test_function():
    assert right_angle_triangle(3, 4, 5) == True, "3^2 + 4^2 = 5^2"
    assert right_angle_triangle(1, 2, 3) == False, "1^2 + 2^2 = 3^2"
    assert right_angle_triangle(4, 5, 6) == False, "4^2 + 5^2 = 6^2"
    assert right_angle_triangle(7, 8, 9) == False, "7^2 + 8^2 = 9^2"
