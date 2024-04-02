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
    return a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a


def test_function():
    assert right_angle_triangle(3, 4, 5) == True, "Invalid result for 3,4,5"
    assert right_angle_triangle(5, 12, 13) == False, "Invalid result for 5,12,13"
    assert right_angle_triangle(7, 24, 25) == True, "Invalid result for 7,24,25"
    assert right_angle_triangle(10, 11, 24) == False, "Invalid result for 10,11,24"
    assert right_angle_triangle(5, 12, 13) == False, "Invalid result for 5,12,13"
    assert right_angle_triangle(9, 12, 15) == True, "Invalid result for 9,12,15"

if __name__ == '__main__':
    test_function()
