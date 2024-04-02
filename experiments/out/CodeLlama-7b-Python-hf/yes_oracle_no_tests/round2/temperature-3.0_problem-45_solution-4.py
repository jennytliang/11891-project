def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Include these tokens in the code: return a * h /
	"""
    return a * h / 2


def square_area(a):
    """Given length of a side return area for a square.
    >>> square_area(5)
    25
    
	Include these tokens in the code: return a * a
	"""
    return a ** 2


def rectangle_area(a, b):
    """Given length and width of a rectangle return area.
    >>> rectangle_area(5, 3)
    15
    
	Include these tokens in the code: return a * b
	"""
    return a * b


def circle_area(r):
    """Given length of a side return area for a circle.
    >>> circle_area(5)
    78.53981633974483
    
	Include these tokens in the code: return 3.14 * r ** 2
	"""
    return 3.14 * r ** 2


def triangle_area_v2(a, b, c):
    """Given length of 3 sides return area for a triangle.
    >>> triangle_area_v2(5, 3, 4)
    6.0
    
	Include these tokens in the code: return 0.5 * p * s
		where p is the perimeter of the triangle, and s is the area
		of a circle with radius equal to the perimeter of the triangle
	"""
    p = a + b + c
    s = 0.5 * p * (p - a) * (p - b) * (p - c)
    return s ** 0.5


def rectangle_area_v2(a, b):
    """Given length and width of a rectangle return area.
    >>> rectangle_area_v2(5, 3)
    15
    
	Include these tokens in the code: return a * b
	"""
    return a * b


def circle_area_v2(r):
    """Given length of a side return area for a circle.
    >>> circle_area_v