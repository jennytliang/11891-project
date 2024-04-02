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
	'''
    if a + b <= c or a + c <= b or b + c <= a:
        return -1
    return (a + b + c) / 2 * (((a + b) ** 2 - (a - b) ** 2) ** 2 + (
        (a + c) ** 2 - (a - c) ** 2) ** 2 + ((b + c) ** 2 - (b - c) ** 2) ** 2) ** 0.5


def test_case(test_number, result, expected):
    print("Test Case #{}:".format(test_number))
    if result == expected:
        print("Passed")
    else:
        print("Failed")


test_case(1, triangle_area(3, 4, 5), 6.00)
test_case(2, triangle_area(1, 2, 10), -1)
test_case(3, triangle_area(10, 10, 10), 0.43)
test_case(4, triangle_area(1, 2, 10), -1)
test_case(5, triangle_area(10, 10, 10), 0.43)
test_case(6, triangle_area(1, 2, 10), -1)
test_case(7, triangle_area(5, 12, 13), 30.00)
test_case(8, triangle_area(7, 24, 25), 52.08)
test_case(9, triangle_area(10, 20, 30), 10.17)
test_case(10, triangle_area(10, 20, 30), 10.17)
test_case(11, triangle_area(10, 20, 30), 10.17)
test_case(12, triangle_area(10, 20, 30), 10.17)
test_case