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

    if 0 <= a <= b + c and b + c >= a and 0 <= b <= c + a and c + a >= b and 0 <= c <= a + b and a + b >= c:
        return 0.5 * (a + b + c)
    else:
        return -1

def test_cases():
    assert triangle_area(3, 4, 5) == 6.00
    assert triangle_area(1, 2, 10) == -1
    assert triangle_area(5, 1, 1) == 4.33
    assert triangle_area(10, 2, 5) == 10.00
    assert triangle_area(10, 5, 5) == 10.00
    assert triangle_area(5, 10, 5) == 10.00
    assert triangle_area(5, 5, 10) == 10.00
    assert triangle_area(1, 2, 1) == -1
    assert triangle_area(1, 1, 1) == -1
    assert triangle_area(1, 1, 2) == -1
    assert triangle_area(1, 2, 2) == -1
    assert triangle_area(2, 1, 2) == -1
    assert triangle_area(2, 2, 1) == -1
    assert triangle_area(2, 2, 2) == -1
    assert triangle_area(1, 3, 3) == -1
    assert triangle_area(3, 1, 3) == -1
    assert triangle_area(3, 3, 1) == -1
    assert triangle_area(3, 3, 3) == -1
    assert triangle_area(3, 4, 5) == 6.00
    assert triangle_area(1, 2, 3) == -1
    assert triangle_area(1, 3, 2) == -1
    assert triangle_area(2, 1, 3) == -