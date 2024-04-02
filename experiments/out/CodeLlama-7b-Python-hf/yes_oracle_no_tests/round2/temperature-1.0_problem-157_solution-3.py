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
    # pass
    return a ** 2 + b ** 2 == c ** 2 # The pythagorean theorem


print('right_angle_triangle(3, 4, 5) =', right_angle_triangle(3, 4, 5))
print('right_angle_triangle(1, 2, 3) =', right_angle_triangle(1, 2, 3))
print('right_angle_triangle(12, 36, 40) =', right_angle_triangle(12, 36, 40))

print('right_angle_triangle(1, 2, -1) =', right_angle_triangle(1, 2, -1))
print('right_angle_triangle(-1, -2, 2) =', right_angle_triangle(-1, -2, 2))
