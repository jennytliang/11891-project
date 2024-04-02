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
    assert right_angle_triangle(7, 24, 25) == False, "7, 24, 25"
    assert right_angle_triangle(13, 12, 15) == False, "13, 12, 15"
    assert right_angle_triangle(10, 20, 20) == True, "10, 20, 20"
    assert right_angle_triangle(5, 12, 13) == False, "5, 12, 13"
    assert right_angle_triangle(7, 24, 26) == False, "7, 24, 26"
    assert right_angle_triangle(10, 10, 10) == True, "10, 10, 10"
    assert right_angle_triangle(5, 24, 25) == True, "5, 24, 25"
    assert right_angle_triangle(8, 15, 17) == False, "8, 15, 17"
    assert right_angle_triangle(7, 24, 25) == False, "7, 24, 25"
    assert right_angle_triangle(6, 8, 10) == False, "6, 8, 10"
    assert right_angle_triangle(5, 12, 13) == False, "5, 12, 13"
    assert right_angle_triangle(8, 17, 17) == False, "8, 17, 17"
    assert right_angle_triangle(10, 20, 30) == False, "10, 20, 30"
    assert right_angle_triangle(8, 