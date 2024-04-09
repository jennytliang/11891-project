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

    ret = (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2)
    return ret


if __name__ == '__main__':
    print("Example:")
    print(right_angle_triangle(3, 4, 5))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(1, 3, 2) == False
    assert right_angle_triangle(5, 12, 13) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")