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
    
	Do not include these tokens in the code: 0 in [ a , b , c ]
	'''


    # Your code here
    if a + b <= c or a + c <= b or b + c <= a:
        return -1
    else:
        return (a * b * c) / 2


def test_function(test_case):
    answer = triangle_area(test_case[0], test_case[1], test_case[2])
    if answer == test_case[3]:
        print("Pass")
    else:
        print("Fail")

test_case_1 = [3, 4, 5, 6.00]
test_case_2 = [1, 1, 1, -1]
test_case_3 = [1, 2, 10, -1]
test_case_4 = [15, 16, 20, 20.27]
test_case_5 = [20, 19, 20, -1]

test_function(test_case_1)
test_function(test_case_2)
test_function(test_case_3)
test_function(test_case_4)
test_function(test_case_5)
