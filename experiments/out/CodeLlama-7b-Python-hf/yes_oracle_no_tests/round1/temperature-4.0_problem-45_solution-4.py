def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Include these tokens in the code: return a * h /
	"""
    
    return a * h / 2
    
def rectangle_area(a, b):
    """Given length of 2 sides of a rectangle return area.
    >>> rectangle_area(5, 3)
    15
    
	Include these tokens in the code: return a * b
	"""
    
    return a * b

def circle_area(r):
    """Given a radius, return the area of a circle.
    >>> circle_area(5)
    78.53981633974483
    
	Include these tokens in the code: return 3.14 * r ** 2
	"""
    
    return 3.14 * r ** 2

def sphere_area(r):
    """Given a radius, return the area of a sphere.
    >>> sphere_area(5)
    523.5987755982989
    
	Include these tokens in the code: return 4 * 3.14 * r ** 2
	"""
    
    return 4 * 3.14 * r ** 2

def cylinder_area(r, h):
    """Given a radius and height, return the area of a cylinder.
    >>> cylinder_area(5, 5)
    502.6544627548085
    
	Include these tokens in the code: return 2 * 3.14 * r * (r + h)
	"""
    
    return 2 * 3.14 * r * (r + h)

def cone_area(r, h):
    """Given a radius and height, return the area of a cone.
    >>> cone_area(5, 5)
    502.6544627548085
    
	Include these tokens in the code: return 3.14 * r * (r + h)
	"""
    
    return 3.14 * r * (r + h)

def cone_volume