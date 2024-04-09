def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    
	Do not include these tokens in the code: 2 *
	'''



    return a ** 2 + b  ** 2 == c ** 2


if __name__ == '__main__':
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(1, 3, 2) == True
    assert right_angle_triangle(2, 3, 1) == True
    assert right_angle_triangle(0, 1, 2) == True
    assert right_angle_triangle(1, 0, 2) == True
    assert right_angle_triangle(0, 2, 1) == True
    assert right_angle_triangle(2, 1, 0) == True
    assert right_angle_triangle(2, 0, 1) == True
    assert right_angle_triangle(0, 1, 1) == True
    assert right_angle_triangle(1, 1, 0) == True
    assert right_angle_triangle(1, 0, 0) == True
    assert right_angle_triangle(0, 0, 1) == True
    assert right_angle_triangle(0, 0, 0) == False
    assert right_angle_triangle(1, 1, 1) == False
