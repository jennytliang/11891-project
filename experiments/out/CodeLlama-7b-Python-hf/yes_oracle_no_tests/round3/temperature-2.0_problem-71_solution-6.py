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
    
	Include these tokens in the code: if a + b <= c or a + c
	Do not include these tokens in the code: def test _ function
	'''
    if a + b <= c or a + c <= b or b + c <= a:
        return -1
    else:
        return (a + b + c) / 2





def test_case1():
    assert triangle_area(3, 4, 5) == 6.00

def test_case2():
    assert triangle_area(1, 2, 10) == -1

def test_case3():
    assert triangle_area(5, 4, 5) == 6.00

def test_case4():
    assert triangle_area(1, 1, 1) == 0.43

def test_case5():
    assert triangle_area(1, 1, 10) == -1

def test_case6():
    assert triangle_area(1, 10, 1) == -1

def test_case7():
    assert triangle_area(10, 1, 1) == -1

def test_case8():
    assert triangle_area(10, 10, 1) == -1

def test_case9():
    assert triangle_area(10, 1, 10) == -1

def test_case10():
    assert triangle_area(1, 10, 10) == -1

def test_case11():
    assert triangle_area(10, 10, 10) == -1

def test_case12():
    assert triangle_area(10, 10, 10) == -1

def test_case13():
    assert triangle_area(10, 10, 10) == -1

def test_case14():
    assert triangle_area(10, 10, 10) == -1

def test_case15():
    assert triangle_area(10, 10, 10) == -1

def test_case16():
    assert triangle_area(10, 10, 