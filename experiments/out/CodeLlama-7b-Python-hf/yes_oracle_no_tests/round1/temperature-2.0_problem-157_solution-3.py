def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    
	Include these tokens in the code: **
	'''

    ret = False
    if a**2 + b**2 == c**2:
        ret = True
    return ret


def test_function():
    assert right_angle_triangle(3, 4, 5) == True, "3^2 + 4^2 = 5^2"
    assert right_angle_triangle(5, 12, 13) == False, "5^2 + 12^2 = 13^2"
    assert right_angle_triangle(7, 24, 25) == True, "7^2 + 24^2 = 25^2"
    assert right_angle_triangle(10, 20, 20) == True, "10^2 + 20^2 = 20^2"
    assert right_angle_triangle(5, 12, 13) == False, "5^2 + 12^2 = 13^2"
    assert right_angle_triangle(9, 12, 15) == False, "9^2 + 12^2 = 15^2"
    assert right_angle_triangle(10, 15, 25) == False, "10^2 + 15^2 = 25^2"
    assert right_angle_triangle(10, 20, 20) == True, "10^2 + 20^2 = 20^2"
    assert right_angle_triangle(10, 20, 21) == False, "10^2 + 20^2 = 21^2"
    assert right_angle_triangle(10, 20, 22) == False, "10^2 + 20^2 = 22^2"
    assert right_angle_triangle(10, 20, 23) == False, "10^2 + 20^2 = 23^2"
    assert right_angle_triangle(10, 20, 24) == False, "10^2 +