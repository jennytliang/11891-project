def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Do not include these tokens in the code: def circle _ area ( r ):
	"""

    return a * h 


def circle_area(r):
    """Given radius of a circle return area for a circle.
    >>> circle_area(5)
    78.53981633974483
    
	Do not include these tokens in the code: def circle _ area ( r ):
	"""

    return 22 / 7 * r ** 2 * 3.1415926535


def rectangle_area(a, b):
    """Given length of a side and high return area for a rectangle.
    >>> rectangle_area(5, 3)
    15
    
	Do not include these tokens in the code: def rectangle _ area ( a, b ):
	"""

    return a * b


def square_area(a):
    """Given length of a side and high return area for a square.
    >>> square_area(5)
    25
    
	Do not include these tokens in the code: def square _ area ( a ):
	"""

    return a * a


def trapezoid_area(a, b, h):
    """Given length of a side and high return area for a trapezoid.
    >>> trapezoid_area(5, 3, 4)
    17.5
    
	Do not include these tokens in the code: def trapezoid _ area ( a, b, h ):
	"""

    return (a + b) / 2 * h


def regular_polygon_area(n, s):
    """Given length of a side and high return area for a regular polygon.
    >>> regular_polygon_area(5, 3)
    10.606601717798212
    
	Do not include these tokens in the code: def regular _ polygon _ area ( n, s ):
	"""

    return (s * n) / 2


def circumference_area(r):
    """Given radius of a circle return area for a circle.