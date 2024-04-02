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
    
	Do not include these tokens in the code: if 0 in [ a
	'''
    # your code here
    if a + b > c and a + c > b and b + c > a:
        return round((a + b + c) / 2 * (((a + b) / 2) * ((a + c) / 2) * ((b + c) / 2)) ** 0.5, 2)
    else:
        return -1


if __name__ == '__main__':
    print("Example:")
    print(triangle_area(3, 4, 5))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert triangle_area(3, 4, 5) == 6.00
    assert triangle_area(1, 2, 10) == -1
    assert triangle_area(10, 20, 30) == 100.00
    assert triangle_area(10, 20, 30) == 100.00
    assert triangle_area(10, 20, 30) == 100.00
    print("Coding complete? Click 'Check' to earn cool rewards!")
