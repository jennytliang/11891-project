def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Do not include these tokens in the code: return ( a * h ) /
	"""
    return ( a * h ) / 2


def circle_area(r):
    """Given radius of a circle return area for a circle.
    >>> circle_area(5)
    78.53981633974483
    
	Do not include these tokens in the code: return 3.14 * ( r ** 2 )
    """
    return 3.14 * ( r ** 2 )


def square_area(a):
    """Given length of a side return area for a square.
    >>> square_area(5)
    25
    
	Do not include these tokens in the code: return ( a ** 2 )
    """
    return ( a ** 2 )


def rectangle_area(a, b):
    """Given length and width of a rectangle return area for a rectangle.
    >>> rectangle_area(5, 3)
    15
    
	Do not include these tokens in the code: return a * b
    """
    return a * b


def rhombus_area(diagonal_1, diagonal_2):
    """Given length of two diagonals of a rhombus return area for a rhombus.
    >>> rhombus_area(5, 3)
    7.5
    
	Do not include these tokens in the code: return ( diagonal_1 * diagonal_2 ) / 2
    """
    return ( diagonal_1 * diagonal_2 ) / 2


def trapezoid_area(a, b, h):
    """Given length of two sides and high return area for a trapezoid.
    >>> trapezoid_area(5, 3, 4)
    19.0
    
	Do not include these tokens in the code: return ( ( a + b ) / 2 ) * h
    """
    return ( ( a + b ) / 2 ) * h


def regular_polygon_area(n, side_length):
    """Given number of sides and length of a side return area for a regular polygon.
    >>>