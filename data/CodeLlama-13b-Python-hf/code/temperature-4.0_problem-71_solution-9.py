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
    '''
    if a > (b + c ) or b > (a + c) or c > (b + a): #not valid
        return -1
    else:
        return round(((a + b + c) / 2)**.5 * 2,2) #calculate herons numerically
#
    return False