def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    
	Include these tokens in the code: 
	'''

    if a**2 + b**2 == c**2:
        return True
    else:
        return False


def test_cases():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(1, 3, 4) == False
    assert right_angle_triangle(5, 6, 7) == False
    assert right_angle_triangle(4, 4, 4) == True
    assert right_angle_triangle(10, 10, 10) == False
    assert right_angle_triangle(2, 2, 2) == True
    assert right_angle_triangle(5, 12, 13) == False
    assert right_angle_triangle(7, 24, 25) == True
    assert right_angle_triangle(10, 20, 25) == False
    assert right_angle_triangle(1, 1, 4) == False
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(1, 2, 3) == False
    print("Test Success!")


if __name__ == "__main__":
    test_cases()
