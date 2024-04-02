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


def test_function():
    assert right_angle_triangle(3, 4, 5) == True, "3^2 + 4^2 = 5^2"
    assert right_angle_triangle(3, 4, 3) == False, "3^2 + 4^2 != 3^2"
    assert right_angle_triangle(1, 2, 3) == False, "1^2 + 2^2 != 3^2"
    assert right_angle_triangle(1, 1, 1) == True, "1^2 + 1^2 = 1^2"
    assert right_angle_triangle(2, 2, 2) == True, "2^2 + 2^2 = 2^2"
    assert right_angle_triangle(10, 20, 10) == True, "10^2 + 20^2 = 10^2"
    assert right_angle_triangle(10, 20, 30) == False, "10^2 + 20^2 != 30^2"


if __name__ == '__main__':
    test_function()
