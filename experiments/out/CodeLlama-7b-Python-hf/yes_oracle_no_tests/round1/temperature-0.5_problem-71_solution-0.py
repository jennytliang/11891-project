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
    
	Include these tokens in the code: <= c or a + c <= b or b
	Do not include these tokens in the code: > and > and
	'''

    if a + b > c and a + c > b and b + c > a:
        return 0.5 * (a + b + c) * (a - b) * (b - c) * (c - a)
    return -1
    
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert triangle_area(3, 4, 5) == 6.00, "Triangle 3-4-5"
    assert triangle_area(2, 2, 2) == 2.00, "Triangle 2-2-2"
    assert triangle_area(3, 4, 5) == -1, "Triangle 3-4-6"
    assert triangle_area(1, 2, 10) == -1, "Triangle 1-2-10"
    assert triangle_area(10, 2, 1) == -1, "Triangle 10-2-1"
    assert triangle_area(10, 2, 2) == 10.00, "Triangle 10-2-2"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
