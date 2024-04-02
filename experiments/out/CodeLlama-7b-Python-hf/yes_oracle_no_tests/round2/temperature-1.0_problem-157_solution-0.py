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

    return a ** 2 + b ** 2 == c ** 2 #True, False, True, False, True


assert(right_angle_triangle(1,2,2) == True)
assert(right_angle_triangle(3,6,6) == False)
assert(right_angle_triangle(3,4,5) == True)
assert(right_angle_triangle(2,2,3) == False)
assert(right_angle_triangle(5,12,13) == True)
assert(right_angle_triangle(5,12,130) == False)
assert(right_angle_triangle(3,4,-80) == True)
assert(right_angle_triangle(3,4,-800) == False)
assert(right_angle_triangle("3",4,-800) == False)
assert(right_angle_triangle("s", "d", "f") == False)
assert(right_angle_triangle(3,4.1,-799.3) == False)
assert(right_angle_triangle(3,4.18,-799.4) == True)
assert(right_angle_triangle(3,4,"5") == False)
assert(right_angle_triangle(1,2) == False)
assert(right_angle_triangle("1","2") == False)
assert(right_angle_triangle(3, 4) == False)
assert(right_angle_triangle(3, 4, 333) == False)
assert(right_angle_triangle(3, 4, 334) == False)
assert(right_angle_triangle(0, 0, 0) == False)
