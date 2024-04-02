def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Include these tokens in the code: return a
	Do not include these tokens in the code: r = (
	"""
    return a * h

def circle_area(r):
    """Given radius of a circle return area for a circle.
    >>> circle_area(3)
    28.274333882308138
    
	Include these tokens in the code: return 3.14
	Do not include these tokens in the code: * r
	"""
    return 3.14 * r * r

def rectangle_area(a, b):
    """Given length of a side and high return area for a rectangle.
    >>> rectangle_area(5, 3)
    15
    
	Include these tokens in the code: return a * b
	Do not include these tokens in the code: * r
	"""
    return a * b

def rhombus_area(a, h):
    """Given length of a side and high return area for a rhombus.
    >>> rhombus_area(5, 3)
    15
    
	Include these tokens in the code: return a * h / 2
	Do not include these tokens in the code: * r
	"""
    return a * h / 2

def trapezoid_area(a, b, h):
    """Given length of a side and high return area for a trapezoid.
    >>> trapezoid_area(5, 3, 4)
    19.0
    
	Include these tokens in the code: return a + b
	Do not include these tokens in the code: * r
	"""
    return (a + b) / 2 * h

def regular_polygon_area(n, r):
    """Given number of sides and radius return area for a regular polygon.
    >>> regular_polygon_area(4, 3)
    12.566370614359172
    >>> regular_polygon_area(10, 5)
    78.56644097187855
    
	Include these tokens in the code: return n *