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
    
	Do not include these tokens in the code: <= c or b + c
	'''

    if  a+b > c and a+c > b and b+c > a:
        return (a+b+c)/2 * (a*b*c)**0.5
    return -1

def test_cases():
    assert triangle_area(3, 4, 5) == 6.00
    assert triangle_area(1, 2, 10) == -1
    assert triangle_area(1, 2, 3) == 4.00
    assert triangle_area(10, 2, 3) == -1
    assert triangle_area(1, 2, 1) == -1
    assert triangle_area(1, 1, 1) == -1
    assert triangle_area(1, 1, 2) == -1
    assert triangle_area(0, 0, 0) == -1
    assert triangle_area(0, 1, 0) == -1
    assert triangle_area(0, 1, 1) == -1
    assert triangle_area(0, 0, 1) == -1
    assert triangle_area(0, 0, 0) == -1
    assert triangle_area(1, 1, 0) == -1
    print("Test Success!")

test_cases()
