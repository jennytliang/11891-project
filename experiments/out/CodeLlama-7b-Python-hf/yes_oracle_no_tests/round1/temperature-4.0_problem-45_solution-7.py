def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Include these tokens in the code: return a * h /
	"""
    return a * h / 2

def rectangle_area(a, b):
    """Given length of two sides return area for a rectangle.
    >>> rectangle_area(5, 3)
    15
    
	Include these tokens in the code: return a * b
	"""
    return a * b

def circle_area(r):
    """Given radius return area for a circle.
    >>> circle_area(5)
    78.53981633974483
    
	Include these tokens in the code: return 3.14 * r * r
	"""
    return 3.14 * r * r

def cylinder_volume(r, h):
    """Given radius and height return volume for a cylinder.
    >>> cylinder_volume(5, 3)
    196.3495408492619
    
	Include these tokens in the code: return 3.14 * r * r * h
	"""
    return 3.14 * r * r * h

def sphere_volume(r):
    """Given radius return volume for a sphere.
    >>> sphere_volume(5)
    418.8799020478639
    
	Include these tokens in the code: return 4/3 * 3.14 * r * r * r
	"""
    return 4/3 * 3.14 * r * r * r

def cone_volume(r, h):
    """Given radius and height return volume for a cone.
    >>> cone_volume(5, 3)
    255.3837910666788
    
	Include these tokens in the code: return 1/3 * 3.14 * r * r * h
	"""
    return 1/3 * 3.14 * r * r * h

def pyramid_volume(a, b, h):
    """Given length of three sides and height return volume for a pyram