def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Include these tokens in the code: a
	Do not include these tokens in the code: (
	"""

    r = a * h / 2
    return r

def triangle_area_v2(a, b, c):
    """Given length of 3 sides return area for a triangle.
    >>> triangle_area_v2(5, 3, 4)
    6.0
    
	Include these tokens in the code: a, b, c
	Do not include these tokens in the code: (
	"""

    p = (a + b + c) / 2
    r = (p * (p-a) * (p-b) * (p-c)) ** 0.5
    return r

def triangle_area_v3(a, b, c):
    """Given length of 3 sides return area for a triangle.
    >>> triangle_area_v3(5, 3, 4)
    6.0
    
	Include these tokens in the code: a, b, c
	Do not include these tokens in the code: (
	"""

    r = a * b * c / (4 * ((a+b+c)/2))
    return r

def rectangle_area(a, b):
    """Given length of 2 sides return area for a rectangle.
    >>> rectangle_area(5, 3)
    15
    
	Include these tokens in the code: a, b
	Do not include these tokens in the code: (
	"""

    r = a * b
    return r

def rectangle_area_v2(a, b):
    """Given length of 2 sides return area for a rectangle.
    >>> rectangle_area_v2(5, 3)
    15
    
	Include these tokens in the code: a, b
	Do not include these tokens in the code: (
	"""

    r = a * b
    return r

def rectangle_area_v3(a, b):
    """Given length of 2 sides return area for a rectangle.
    >>> rectangle_area_v3(5, 3)
    15
    
	Include these tokens in the code: a, b
