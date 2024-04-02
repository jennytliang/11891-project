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

    if 0 < a <= b + c and 0 < b <= a + c and 0 < c <= a + b:
        p = (a+b+c)/2
        area = (p*(p-a)*(p-b)*(p-c))**0.5
        return round(area, 2)
    else:
        return -1

print(triangle_area(3, 4, 5)) # == 6.00 
print(triangle_area(1, 2, 10)) # == -1
print(triangle_area(10, 1, 1)) # == -1
