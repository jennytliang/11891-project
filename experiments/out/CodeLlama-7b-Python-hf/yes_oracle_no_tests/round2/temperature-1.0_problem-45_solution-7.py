def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r = 0 . 5
	"""
    r = 0.5 * a * h
    return r

print(triangle_area(5, 3))

def rectangle_area(a, b):
    """Given length of one side and another return area for a rectangle.
    >>> rectangle_area(5, 3)
    15
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r = a * b
	"""
    r = a * b
    return r

print(rectangle_area(5, 3))

def circle_area(r):
    """Given radius return area for a circle.
    >>> circle_area(5)
    78.53981633974483
    
	Include these tokens in the code: return
	Do not include these tokens in the code: pi = 3.14
	"""
    pi = 3.14
    r = pi * (r ** 2)
    return r

print(circle_area(5))

def trapezoid_area(a, b, h):
    """Given length of two sides and high return area for a trapezoid.
    >>> trapezoid_area(5, 3, 1)
    7.5
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r = 0.5
	"""
    r = 0.5 * (a + b) * h
    return r

print(trapezoid_area(5, 3, 1))

def regular_polygon_area(n, side):
    """Given number of sides and side length return area for a regular polygon.
    >>> regular_polygon_area(5, 3)
    10.866025403784438
    
	Include these tokens in the code: return
	Do not include these tokens in the code: pi = 3.14
	"""
    pi = 3.14
    r = (pi * (side ** 2