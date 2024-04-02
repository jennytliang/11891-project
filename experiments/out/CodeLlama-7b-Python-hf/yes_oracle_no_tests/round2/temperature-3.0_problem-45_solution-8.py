def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Do not include these tokens in the code: r = 0 . 5
	"""
    return a * h / 2.0


def triangle_area_with_side_and_base(side, base):
    """Given length of side and base return area for a triangle.
    >>> triangle_area_with_side_and_base(5, 3)
    7.5
    
	Do not include these tokens in the code: r = 0 . 5
	"""
    return side * base / 2.0


def triangle_area_with_three_sides(a, b, c):
    """Given length of three sides of a triangle, return area for a triangle.
    >>> triangle_area_with_three_sides(5, 3, 4)
    6.0
    
	Do not include these tokens in the code: r = 0 . 5
	"""
    s = (a + b + c) / 2.0
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5


def triangle_area_with_three_sides_and_angles(a, b, c, alpha, beta, gamma):
    """Given length of three sides of a triangle, return area for a triangle.
    >>> triangle_area_with_three_sides_and_angles(5, 3, 4, 60, 30, 90)
    6.0
    
	Do not include these tokens in the code: r = 0 . 5
	"""
    s = (a + b + c) / 2.0
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5


def trapezoid_area(a, b, h):
    """Given length of two sides and high return area for a trapezoid.
    >>> trapezoid_area(5, 3, 3)
    6.0
    
	Do not include these tokens in the code: r = 0 . 5
	"""
    return (a + b) * h / 2