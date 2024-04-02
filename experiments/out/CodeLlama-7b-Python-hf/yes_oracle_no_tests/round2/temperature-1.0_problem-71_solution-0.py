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
    
	Include these tokens in the code: a + b <= c or a + c <=
	Do not include these tokens in the code: ( )> = and (
	'''




def test_triangle_area_case_1():
    assert triangle_area(3, 4, 5) == 6.00

def test_triangle_area_case_2():
    assert triangle_area(10, 2, 5) == 10.00

def test_triangle_area_case_3():
    assert triangle_area(3, 4, 5) == 6.00

def test_triangle_area_case_4():
    assert triangle_area(5, 12, 13) == 38.40

def test_triangle_area_case_5():
    assert triangle_area(22, 20, 20) == 84.00


def test_triangle_area_case_6():
    assert triangle_area(9.9, 10.3, 10.4) == 52.42


def test_triangle_area_case_7():
    assert triangle_area(2.3, 4.3, 21.6) == -1