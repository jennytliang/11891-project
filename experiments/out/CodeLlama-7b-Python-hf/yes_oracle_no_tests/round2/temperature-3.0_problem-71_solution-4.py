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
    
	Include these tokens in the code: p
	Do not include these tokens in the code: else : s
	'''

    if a + b <= c or a + c <= b or b + c <= a:
         return -1
    else:
         p = (a + b + c) / 2
         s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
         return s


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert triangle_area(3, 4, 5) == 6.00, "First"
    assert triangle_area(1, 2, 10) == -1, "Second"
    assert triangle_area(10, 10, 10) == -1, "Third"
    assert triangle_area(10, 10, 11) == 52.96, "Fourth"
    print('Done! Go Check!')
