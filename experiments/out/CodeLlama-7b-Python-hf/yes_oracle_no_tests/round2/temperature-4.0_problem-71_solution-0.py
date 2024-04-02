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


    if a + b <= c:
        return -1
    elif b + c <= a:
        return -1
    elif c + a <= b:
        return -1
    else:
        s = (a + b + c)/2
        return (s*(s-a)*(s-b)*(s-c))**0.5


assert triangle_area(3, 4, 5) == 6.00, 'triangle_area(3, 4, 5) == 6.00'
assert triangle_area(1, 2, 10) == -1, 'triangle_area(1, 2, 10) == -1'
assert triangle_area(10, 2, 1) == 10.0, 'triangle_area(10, 2, 1) == 10.0'
assert triangle_area(5, 1, 5) == 5.00, 'triangle_area(5, 1, 5) == 5.00'
assert triangle_area(5, 1, 6) == -1, 'triangle_area(5, 1, 6) == -1'
assert triangle_area(1, 2, 2) == 1.73, 'triangle_area(1, 2, 2) == 1.73'
assert triangle_area(1, 3, 2) == 2.00, 'triangle_area(1, 3, 2) == 2.00'
