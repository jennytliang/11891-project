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
    
	Include these tokens in the code: + b
	'''


  
def test_function():
    assert triangle_area(3, 4, 5) == 6.00
    assert triangle_area(1, 2, 10) == -1
    assert triangle_area(10, 10, 10) == -1
    assert triangle_area(1, 1, 1) == -1
    assert triangle_area(1, 2, 2) == 0.50
    assert triangle_area(7, 2, 2) == 1.00
    assert triangle_area(5, 12, 13) == 31.00
    assert triangle_area(7, 8, 10) == 20.00

if __name__ == '__main__':
    test_function()
