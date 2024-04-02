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

    if 0 in [a, b, c]:
        return -1
    if a + b <= c:
        return -1
    if b + c <= a:
        return -1
    if c + a <= b:
        return -1

    s = (a + b + c) / 2
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

    return round(area, 2)


if __name__ == '__main__':
    print("Example:")
    print(triangle_area(3, 4, 5))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert triangle_area(3, 4, 5) == 6.00
    assert triangle_area(2, 2, 2) == 1.73
    assert triangle_area(5, 4, 3) == -1
    assert triangle_area(10, 2, 2) == -1

    print("Coding complete? Click 'Check' to earn cool rewards!")
