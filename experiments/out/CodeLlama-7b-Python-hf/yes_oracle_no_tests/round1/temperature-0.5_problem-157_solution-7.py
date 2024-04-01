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

    # we know that the sum of the lengths of any two sides of a triangle must be greater than or equal to the length of the remaining side.
    # if a + b > c and a + c > b and b + c > a
    # return True
    # else
    # return False
    return a + b > c and a + c > b and b + c > a


print(right_angle_triangle(3, 4, 5))
print(right_angle_triangle(1, 2, 3))
