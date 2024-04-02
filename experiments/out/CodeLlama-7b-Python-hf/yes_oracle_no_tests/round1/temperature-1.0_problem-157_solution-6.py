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
    # YOUR CODE HERE
    if a**2 + b**2 == c**2:
        return True
    else:
        return False


# TESTS
# Put some tests below, they will only be evaluated if you call
# test() explicitly.

print ("right_angle_triangle(3, 4, 5)")
print (right_angle_triangle(3, 4, 5))
print ("right_angle_triangle(1, 2, 3)")
print (right_angle_triangle(1, 2, 3))
print ("right_angle_triangle(1, 1, 1)")
print (right_angle_triangle(1, 1, 1))


# print ("right_angle_triangle(3, 4, 5)")
# print (right_angle_triangle(3, 4, 5))
# print ("right_angle_triangle(1, 2, 3)")
# print (right_angle_triangle(1, 2, 3))
# print ("right_angle_triangle(1, 1, 1)")
# print (right_angle_triangle(1, 1, 1))
