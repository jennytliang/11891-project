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

def test_case(a, b, c, solution, test_func):

    output = test_func(a, b, c)
    if output == solution:
        print("Test case passed!")
    else:
        print("Test case failed!")

    print("{}, {}, {}: {}".format(a, b, c, output))
    print("Solution: {}\n".format(solution))


test_case(3, 4, 5, True, right_angle_triangle)
test_case(2, 3, 2, False, right_angle_triangle)
test_case(3, 4, 3, False, right_angle_triangle)
test_case(1, 2, 1, False, right_angle_triangle)
