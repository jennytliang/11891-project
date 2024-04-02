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
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(5, 12, 13) == False
    assert right_angle_triangle(7, 24, 25) == True
    assert right_angle_triangle(13, 16, 20) == True
    assert right_angle_triangle(5, 12, 13) == False
    assert right_angle_triangle(2, 2, 2) == False
    assert right_angle_triangle(10, 20, 20) == True
    assert right_angle_triangle(10, 15, 20) == True
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(5, 12, 13) == False
    assert right_angle_triangle(7, 24, 25) == True
    assert right_angle_triangle(13, 16, 20) == True
    assert right_angle_triangle(5, 12, 13) == False
    assert right_angle_triangle(2, 2, 2) == False
    assert right_angle_triangle(10, 20, 20) == True
    assert right_angle_triangle(10, 15, 20) == True
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(5, 12, 13) == False
    assert right_angle_triangle(7, 24, 25) == True
    assert right_angle_triangle(13, 16, 20) == True
   