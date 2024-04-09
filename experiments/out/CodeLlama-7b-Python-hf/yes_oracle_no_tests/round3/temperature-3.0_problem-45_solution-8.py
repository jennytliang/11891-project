def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Do not include these tokens in the code: . 0
	"""

    return a * 0.5 * h


def trapezium_area(a, b, h):
    """Given two side and high return area for a trapezium.
    >>> trapezium_area(10, 12, 3)
    42.0
    
	Do not include these tokens in the code: . 0
	"""

    return 0.5 * (a + b) * h


def circle_area(r):
    """Given radius return area for a circle.
    >>> circle_area(5)
    78.53981633974483
    
	Do not include these tokens in the code: . 0
	"""

    return 0.25 * 3.14 * r ** 2


def rhombus_area(d1, d2):
    """Given two diagonals return area for a rhombus.
    >>> rhombus_area(10, 12)
    60.0
    
	Do not include these tokens in the code: . 0
	"""

    return 0.5 * d1 * d2


def parallelogram_area(b, h):
    """Given base and high return area for a parallelogram.
    >>> parallelogram_area(10, 20)
    200.0
    
	Do not include these tokens in the code: . 0
	"""

    return b * h


def kite_area(d1, d2):
    """Given two diagonals return area for a kite.
    >>> kite_area(10, 20)
    50.0
    
	Do not include these tokens in the code: . 0
	"""

    return 0.5 * d1 * d2


def regular_polygon_area(n, s):
    """Given number of sides and side length return area for a regular polygon.
    >>> regular_polygon_area(10, 2)
    10