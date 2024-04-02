def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Include these tokens in the code: return a * h /
	"""
    return a * h / 2

def rectangle_area(w, h):
    """Given width and high return area for a rectangle.
    >>> rectangle_area(5, 3)
    15
    
	Include these tokens in the code: return w * h
	"""
    return w * h

def circle_area(r):
    """Given radius, return area for a circle.
    >>> circle_area(5)
    78.53981633974483
    
	Include these tokens in the code: return 3.14 * r ** 2
	"""
    return 3.14 * r ** 2

def sphere_area(r):
    """Given radius, return area for a sphere.
    >>> sphere_area(5)
    523.5987755982989
    
	Include these tokens in the code: return 4 * 3.14 * r ** 2
	"""
    return 4 * 3.14 * r ** 2

def cube_area(a):
    """Given side length, return area for a cube.
    >>> cube_area(5)
    150
    
	Include these tokens in the code: return 6 * a ** 2
	"""
    return 6 * a ** 2

def pyramid_area(b, h):
    """Given base and height, return area for a pyramid.
    >>> pyramid_area(5, 3)
    75
    
	Include these tokens in the code: return b ** 2 + h ** 2
	"""
    return b ** 2 + h ** 2

def cone_area(r, h):
    """Given radius and height, return area for a cone.
    >>> cone_area(5, 3)
    63.61338746135389
    
	Include these tokens in the code: return pi * r * (r + h)
	"""
    return 3