def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    
	Do not include these tokens in the code: # code goes here
	'''
    # code goes here
    return a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2

if __name__ == '__main__':
    # Test your code
    # Test Case 1
    print ('Test Case 1 Result \t\t\t\t' + str(right_angle_triangle(3, 4, 5)))
    print ('Test Case 2 \t\t\t\t\t\t' + str(right_angle_triangle(1, 2, 3)))
    print ('Test Case 3 \t\t\t\t\t\t' + str(right_angle_triangle(4, 5, 6)))
    print ('Test Case 4 \t\t\t\t\t\t' + str(right_angle_triangle(10, 10, 17)))
    print ('Test Case 5 \t\t\t\t\t\t' + str(right_angle_triangle(7, 24, 25)))
    print ('Test Case 6 \t\t\t\t\t\t' + str(right_angle_triangle(13, 14, 15)))
