def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    
	Do not include these tokens in the code: #
	'''
    # Your code here
    if (a*a)+(b*b) == (c*c):
        return True
    else:
        return False


def test_function():
    assert right_angle_triangle(3, 4, 5) == True, "Basic"
    assert right_angle_triangle(10, 20, 20) == False, "Right angle"
    assert right_angle_triangle(1, 2, 3) == False, "Not right angle"
    assert right_angle_triangle(3, 1, 2) == False, "Not right angle"
    assert right_angle_triangle(3, 2, 1) == False, "Not right angle"
    assert right_angle_triangle(2, 3, 1) == False, "Not right angle"
    assert right_angle_triangle(1, 3, 2) == False, "Not right angle"
    assert right_angle_triangle(2, 1, 3) == False, "Not right angle"
    
    assert right_angle_triangle(1, 1, 1) == False, "Not right angle"
    assert right_angle_triangle(2, 2, 2) == False, "Not right angle"
    assert right_angle_triangle(3, 3, 3) == False, "Not right angle"
    assert right_angle_triangle(4, 4, 4) == False, "Not right angle"
    assert right_angle_triangle(5, 5, 5) == False, "Not right angle"
    assert right_angle_triangle(6, 6, 6) == False, "Not right angle"
    assert right_angle_triangle(7, 7, 7) == False, "Not right angle"
    assert right_angle_triangle(8, 8, 8) == False, "Not right angle"
    assert right_angle_triangle(9, 9, 9) == False, "Not right angle"
    
if __name__ == '__main__':
    test_function()
