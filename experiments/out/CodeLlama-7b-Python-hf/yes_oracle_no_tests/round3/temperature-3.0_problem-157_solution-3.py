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
    if a ** 2 + b ** 2 == c ** 2:
        return True
    else:
        return False


def test_function():
    assert right_angle_triangle(3, 4, 5) == True, "3^2 + 4^2 = 5^2"
    assert right_angle_triangle(5, 12, 13) == False, "5^2 + 12^2 != 13^2"
    assert right_angle_triangle(7, 24, 25) == True, "7^2 + 24^2 = 25^2"
    assert right_angle_triangle(10, 20, 20) == False, "There is no right-angled triangle with two sides being equal."
    assert right_angle_triangle(10, 20, 30) == False, "30 is not a square number"


if __name__ == '__main__':
    test_function()
