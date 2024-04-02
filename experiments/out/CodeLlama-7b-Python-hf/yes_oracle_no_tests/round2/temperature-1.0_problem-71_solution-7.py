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
    
	Do not include these tokens in the code: ( a <= 0 ) or ( b
	'''


def is_triangle_valid(a, b, c):
    return a + b > c and b + c > a and a + c > b


def area_triangle(a, b, c):
    return math.sqrt(
        pow(c, 2)
        - (pow(a, 2) + pow(b, 2) - pow(c, 2)) / 2
    )

