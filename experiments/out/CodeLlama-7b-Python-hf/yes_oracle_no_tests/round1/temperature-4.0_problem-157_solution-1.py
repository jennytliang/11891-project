def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    
	Do not include these tokens in the code: if a > b and a >
	'''
    return a**2 + b**2 == c**2


def test_function():
    assert right_angle_triangle(3, 4, 5) == True, "Three side 3,4,5"
    assert right_angle_triangle(7, 24, 25) == True, "Three side 7,24,25"
    assert right_angle_triangle(5, 12, 13) == False, "Three side 5,12,13"
    assert right_angle_triangle(7, 24, 26) == False, "Three side 7,24,26"
    assert right_angle_triangle(13, 12, 10) == False, "Three side 13,12,10"
    assert right_angle_triangle(4, 5, 6) == False, "Three side 4,5,6"
    assert right_angle_triangle(10, 10, 10) == False, "Three side 10,10,10"
    assert right_angle_triangle(10, 10, 11) == False, "Three side 10,10,11"

if __name__ == '__main__':
    test_function()