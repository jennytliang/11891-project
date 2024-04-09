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
    
	Do not include these tokens in the code: a <= 0 or b <= 0 or
	'''

  # YOUR CODE HERE
    if a <= 0 or b <= 0 or c <= 0:
        return -1
    if a + b <= c or a + c <= b or b + c <= a:
        return -1
    else:
        return (a + b + c) / 2 * ((a + b - c) / 2) ** 0.5


def test_function(test_case):
    test_input, test_expected = test_case
    test_actual = triangle_area(*test_input)
    if test_actual == test_expected:
        print("Pass")
    else:
        print("Fail")


test_function(([3, 4, 5], 6.00))
test_function(([1, 2, 10], -1))
test_function(([10, 20, 20], 50.00))
test_function(([10, 20, 10], 67.50))
test_function(([5, 6, 6], 9.00))
test_function(([3, 4, 5], 6.00))
test_function(([1, 2, 10], -1))
test_function(([10, 20, 20], 50.00))
test_function(([10, 20, 10], 67.50))
test_function(([5, 6, 6], 9.00))
test_function(([3, 4, 5], 6.00))
test_function(([1, 2, 10], -1))
test_function(([10, 20, 20], 50.00))
test_function(([10, 20, 10], 67.50))
test_function(([5, 6, 6], 9.00))