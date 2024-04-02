def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Include these tokens in the code: a
	Do not include these tokens in the code: (
	"""

    r = a * h / 2
    return r

def square_area(a):
    """Given length of a side return area for a square.
    >>> square_area(5)
    25
    
	Include these tokens in the code: a
	Do not include these tokens in the code: (
	"""

    r = a * a
    return r

def rectangle_area(a, b):
    """Given length and width of a rectangle return area for a rectangle.
    >>> rectangle_area(5, 3)
    15
    
	Include these tokens in the code: a, b
	Do not include these tokens in the code: (
	"""

    r = a * b
    return r

def rhombus_area(a, h):
    """Given length of diagonals and high return area for a rhombus.
    >>> rhombus_area(5, 3)
    13.75
    
	Include these tokens in the code: a, h
	Do not include these tokens in the code: (
	"""

    r = a * h / 2
    return r

def trapezoid_area(a, b, h):
    """Given length of bases, high and height return area for a trapezoid.
    >>> trapezoid_area(5, 3, 2)
    11.25
    
	Include these tokens in the code: a, b, h
	Do not include these tokens in the code: (
	"""

    r = (a + b) / 2 * h
    return r

def regular_polygon_area(d, n):
    """Given length of side and number of sides return area for a regular polygon.
    >>> regular_polygon_area(4, 4)
    16.0
    
	Include these tokens in the code: d, n
	Do not include these tokens in the code: (
	"""

    r = d * d * 3.14159265359 / 2 / n
   