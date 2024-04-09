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



    i = 0
    if a <= b + c and b <= a + c and c <= a + b:
        i = 1

    if i == 1:
        return round((1/2) * (a + b + c) * (math.sqrt(1/4 * (-a + b + c)*(-a + b + c) + 2 * (a * b) + 2 * (a * c) + 2 * (b * c))), 2)
    else:
        return -1
    



    
# Pybites solution

import math

def triangle_area(a, b, c):
    """Given the lengths of the three sides of a triangle. 
    Return the area of the triangle rounded to 2 decimal points 
    if the three sides form a valid triangle. Otherwise return -1
    Three sides make a valid triangle when the sum of any two sides 
    is greater than the third side.
    Example:
    triangle_area(3, 4, 5) == 6.00
    triangle_area(1, 2, 10) == -1
    """

    if a + b <= c or a + c <= b or b + c <= a:
        return -1
    s = (a + b + c) / 2
    return round(math.sqrt(s * (s - a) * (s - b) * (s - c)), 2)
