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
    assert right_angle_triangle(3, 4, 5) == True, "3^2 + 4^2 = 25 + 16 = 41 = 5^2"
    assert right_angle_triangle(1, 2, 3) == False, "1^2 + 2^2 = 1 + 4 = 5 != 3^2"
    assert right_angle_triangle(8, 15, 17) == False, "8^2 + 15^2 = 64 + 225 = 289 != 17^2"
    assert right_angle_triangle(84, 87, 90) == True, "84^2 + 87^2 = 7156 + 7809 = 15025 = 90^2"
    assert right_angle_triangle(5, 6, 7) == False, "5^2 + 6^2 = 25 + 36 = 61 != 7^2"
    assert right_angle_triangle(7, 8, 9) == False, "7^2 + 8^2 = 49 + 64 = 113 != 9^2"
    assert right_angle_triangle(10, 20, 25) == True, "10^2 + 20^2 = 100 + 400 = 500 = 25^2"

if __name__ == '__main__':
    test_function()