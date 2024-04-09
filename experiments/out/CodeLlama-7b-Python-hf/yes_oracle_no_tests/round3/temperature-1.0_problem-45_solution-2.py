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
    """Given side length return area for a square.
    >>> square_area(5)
    25
    
	Include these tokens in the code: a
	Do not include these tokens in the code: (
	"""

    r = a * a
    return r


def rectangle_area(a, b):
    """Given length of two sides return area for a rectangle.
    >>> rectangle_area(5, 3)
    15
    
	Include these tokens in the code: a, b
	Do not include these tokens in the code: (
	"""

    r = a * b
    return r


def rhombus_area(a, h):
    """Given length of diagonals return area for a rhombus.
    >>> rhombus_area(5, 3)
    15
    
	Include these tokens in the code: a
	Do not include these tokens in the code: (
	"""

    r = a * h / 2
    return r


def trapezoid_area(a, b, h):
    """Given length of two bases and high return area for a trapezoid.
    >>> trapezoid_area(5, 3, 2)
    11.25
    
	Include these tokens in the code: a, b
	Do not include these tokens in the code: (
	"""

    r = (a + b) / 2 * h
    return r


def regular_polygon_area(n, side):
    """Given number of sides and side length return area for a regular polygon.
    >>> regular_polygon_area(4, 3)
    12.5
    
	Include these tokens in the code: n, side
	Do not include these tokens in the code: (
	"""

    r = (n * side * side) / (4 * math.tan(math.pi / n))
    return r
