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


    if (a <= 0) or (b <= 0) or (c <= 0):
        return -1
    elif (a + b <= c) or (b + c <= a) or (a + c <= b):
        return -1
    else:
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        return round(area, 2)


def test_cases():
    assert triangle_area(3, 4, 5) == 6.00
    assert triangle_area(1, 2, 10) == -1
    assert triangle_area(10, 2, 1) == -1
    assert triangle_area(10, 2, 10) == -1
    assert triangle_area(10, 10, 1) == -1
    assert triangle_area(0, 0, 0) == -1
    assert triangle_area(-1, 2, 10) == -1
    assert triangle_area(1, -2, 10) == -1
    assert triangle_area(1, 2, -10) == -1
    print("Test Success!")

test_cases()
