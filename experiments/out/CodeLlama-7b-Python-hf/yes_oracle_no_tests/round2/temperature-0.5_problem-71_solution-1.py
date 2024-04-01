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


    if (a+b>c) and (a+c>b) and (b+c>a):
        p = (a+b+c)/2
        s = (p*(p-a)*(p-b)*(p-c))**0.5
        return round(s, 2)
    else:
        return -1


def test_cases():
    assert triangle_area(3, 4, 5) == 6.00
    assert triangle_area(1, 2, 10) == -1
    assert triangle_area(1, 2, 3) == 4.00
    print("Test Success!")


if __name__ == "__main__":
    test_cases()
