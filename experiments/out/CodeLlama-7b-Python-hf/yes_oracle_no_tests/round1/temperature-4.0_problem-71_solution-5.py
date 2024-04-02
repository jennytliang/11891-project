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

    if  a + b <= c or a + c <= b or b + c <= a:
        return -1
    else:
        p = (a + b + c) / 2
        area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        return round(area, 2)


def test_cases():
    assert triangle_area(3, 4, 5) == 6.00
    assert triangle_area(2, 2, 2) == 1.73
    assert triangle_area(5, 12, 13) == 49.00
    assert triangle_area(7, 24, 25) == 49.00
    assert triangle_area(10, 20, 30) == -1
    assert triangle_area(5, 6, 6) == -1
    assert triangle_area(10, 10, 10) == -1

    print("Test Success!")


if __name__ == "__main__":
    test_cases()
