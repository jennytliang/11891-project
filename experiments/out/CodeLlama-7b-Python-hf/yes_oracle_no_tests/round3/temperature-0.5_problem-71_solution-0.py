def triangle_area(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return the area of
    the triangle rounded to 2 decimal points if the three sides form a valid triangle. 
    Otherwise return -1
    Three sides make a valid triangle when the sum of any two sides is greater 
    than the third side.
    Example:
    triangle_area(3, 4, 5) == 6.00
    triangle_area(1, 2, 10) == -1
    
	Include these tokens in the code: a + b
	Do not include these tokens in the code: (
	'''


    if a + b <= c:
        return -1
    elif a + c <= b:
        return -1
    elif b + c <= a:
        return -1
    else:
        return 0.5 * a * b

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    