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

def test_cases():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(1, 1, 1) == True
    assert right_angle_triangle(1, 1, 2) == False
    assert right_angle_triangle(1, 2, 1) == True
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(2, 2, 2) == True
    assert right_angle_triangle(5, 12, 13) == False
    assert right_angle_triangle(8, 15, 17) == True
    assert right_angle_triangle(10, 22, 28) == False
    assert right_angle_triangle(27, 30, 36) == True
    assert right_angle_triangle(1, 1, 3) == False
    assert right_angle_triangle(1, 3, 1) == False
    assert right_angle_triangle(3, 1, 1) == False
    print("Test Success!")


if __name__ == "__main__":
    test_cases()
