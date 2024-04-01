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

    # add code here
    return (a**2 + b**2) == c**2 or (a**2 + c**2) == b**2 or (b**2 + c**2) == a**2


# tests
if __name__ == '__main__':
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(1, 3, 2) == True
    assert right_angle_triangle(2, 3, 1) == True
    assert right_angle_triangle(3, 2, 1) == True
    assert right_angle_triangle(5, 12, 13) == False
    assert right_angle_triangle(7, 24, 25) == True
    assert right_angle_triangle(10, 8, 17) == False
    assert right_angle_triangle(5, 12, 13) == False
    assert right_angle_triangle(7, 24, 25) == True
    assert right_angle_triangle(10, 8, 17) == False
    print('Passed all tests.')


# Test case 1:
# Enter your code here.
# a = 3
# b = 4
# c = 5

# Test case 2:
# Enter your code here.
# a = 1
# b = 2
# c = 3

# Test case 3:
# Enter your code here.
# a = 5
# b = 12
# c = 13

# Test case 4:
# Enter your code here.
# a = 7
# b = 24
# c = 25

# Test case 5:
# Enter your code here.
# a = 10
# b = 8
# c = 17
