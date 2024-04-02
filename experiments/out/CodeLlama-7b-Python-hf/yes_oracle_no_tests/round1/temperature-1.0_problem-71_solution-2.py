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
    
	Include these tokens in the code: <=
	Do not include these tokens in the code: >
	'''

    if 0 <= a + b <= c or 0 <= a + c <= b or 0 <= b + c <= a:
        s = (a + b + c)/2
        return (s*(s-a)*(s-b)*(s-c))**0.5
    else:
        return -1


print(triangle_area(3, 4, 5))
print(triangle_area(1, 2, 10))