def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    
	Include these tokens in the code: or
	Do not include these tokens in the code: # print ( right _ angle _ triangle
	'''

    return a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + c ** 2 == a ** 2


def is_int(num):
    try:
        return int(num)
    except:
        return False


def is_float(num):
    try:
        return float(num)
    except:
        return False


def is_number(num):
    return is_int(num) or is_float(num)


def is_positive(num):
    return num > 0


def is_right_angle_triangle(a, b, c):
    return is_number(a) and is_number(b) and is_number(c) and is_positive(a) and is_positive(b) and is_positive(c) and right_angle_triangle(a, b, c)


def test_is_right_angle_triangle():
    assert is_right_angle_triangle(3, 4, 5) == True
    assert is_right_angle_triangle(1, 2, 3) == False


test_is_right_angle_triangle()
