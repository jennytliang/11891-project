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

if __name__ == '__main__':
    print("Example:")
    print(right_angle_triangle(3, 4, 5))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(3, 4, 3) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")