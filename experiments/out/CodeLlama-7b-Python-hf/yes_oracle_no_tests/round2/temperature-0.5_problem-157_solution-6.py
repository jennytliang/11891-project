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


    reta = (a**2 + b**2 - c**2)
    retb = (a**2 + c**2 - b**2)
    retc = (b**2 + c**2 - a**2)

    if reta == 0 or retb == 0 or retc == 0:
        return True
    else:
        return False

print(right_angle_triangle(3, 4, 5))
print(right_angle_triangle(1, 2, 3))