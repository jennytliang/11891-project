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
    assert right_angle_triangle(3, 4, 5) == True, "3, 4, 5"
    assert right_angle_triangle(4, 3, 5) == True, "4, 3, 5"
    assert right_angle_triangle(5, 4, 3) == True, "5, 4, 3"
    assert right_angle_triangle(3, 5, 4) == True, "3, 5, 4"
    assert right_angle_triangle(4, 5, 3) == True, "4, 5, 3"
    assert right_angle_triangle(5, 3, 4) == True, "5, 3, 4"
    assert right_angle_triangle(3, 4, 6) == False, "3, 4, 6"
    assert right_angle_triangle(4, 6, 3) == False, "4, 6, 3"
    assert right_angle_triangle(6, 3, 4) == False, "6, 3, 4"
    assert right_angle_triangle(3, 6, 4) == False, "3, 6, 4"
    assert right_angle_triangle(6, 4, 3) == False, "6, 4, 3"
    assert right_angle_triangle(4, 3, 6) == False, "4, 3, 6"
    assert right_angle_triangle(1, 2, 3) == False, "1, 2, 3"
    assert right_angle_triangle(1, 3, 2) == False, "1, 3, 2"
    assert right_angle_triangle(2, 1, 3) == False, "2, 1, 3"
    assert right_angle_triangle(2, 3, 1) == False, "2, 3, 1"
    assert right_angle_triangle(3, 