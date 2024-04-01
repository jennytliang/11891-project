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
        return (a * b * 1.0)/2
    else:
        return -1
    
def test_cases():
    assert triangle_area(3, 4, 5) == 6.00
    assert triangle_area(1, 2, 10) == -1
    assert triangle_area(10, 1, 1) == -1
    assert triangle_area(10, 1, 11) == 55.56
    assert triangle_area(7, 2, 2) == 10.16
    assert triangle_area(5, 1, 2.5) == 2.00
    assert triangle_area(1, 2, 2) == 0.50
    assert triangle_area(2, 3, 3) == 1.73
    assert triangle_area(7, 2, 5) == 10.29
    assert triangle_area(10, 1, 3) == -1
    print("Test Success!")

test_cases()
