def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    
	Do not include these tokens in the code: # pass
	'''
    return a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2


if __name__ == '__main__':
    assert right_angle_triangle(3, 4, 5), "3, 4, 5 are not the sides of a right-angled triangle"
    assert not right_angle_triangle(1, 2, 3), "1, 2, 3 are not the sides of a right-angled triangle"
    assert not right_angle_triangle(7, 24, 25), "7, 24, 25 are not the sides of a right-angled triangle"
    assert right_angle_triangle(2, 2, 2), "2, 2, 2 are not the sides of a right-angled triangle"
    assert right_angle_triangle(12, 16, 15), "12, 16, 15 are not the sides of a right-angled triangle"
