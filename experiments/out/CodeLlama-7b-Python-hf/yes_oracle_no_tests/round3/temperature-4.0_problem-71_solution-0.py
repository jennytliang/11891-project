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
    
	Include these tokens in the code: or a + c <= b or
	Do not include these tokens in the code: : return - 1 elif
	'''



    if a + b <= c or a + c <= b or b + c <= a:
        return -1
    else:
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c))**0.5
        return round(area, 2)


assert(triangle_area(3, 4, 5) == 6.00)
assert(triangle_area(1, 2, 10) == -1)
assert(triangle_area(10, 2, 4) == 10.00)
assert(triangle_area(10, 2, 5) == -1)
assert(triangle_area(10, 2, 2) == 4.24)
assert(triangle_area(10, 1, 2) == 3.73)
assert(triangle_area(1, 1, 2) == 1.00)
assert(triangle_area(1, 1, 1) == 0.43)
assert(triangle_area(1, 2, 2) == 1.50)
assert(triangle_area(2, 2, 2) == 1.73)
assert(triangle_area(1, 2, 3) == -1)
assert(triangle_area(1, 3, 3) == -1)
assert(triangle_area(3, 2, 1) == -1)
assert(triangle_area(1, 2, 1) == -1)
assert(triangle_area(1, 1, 1) == 0.43)
assert(triangle_area(2, 2, 2) == 1.73)
assert(triangle_area(1, 1, 2) == 3.73)
assert(triangle_area(1, 2, 1) == 2.00)
assert(triangle_area(2, 1, 1) == 2.00)
assert(triangle_area(1, 2, 2) == 1