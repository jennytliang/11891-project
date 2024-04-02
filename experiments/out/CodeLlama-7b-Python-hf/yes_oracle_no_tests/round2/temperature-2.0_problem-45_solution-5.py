def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""
    return (a * h) / 2

def rectangle_area(a, b):
    """Given length and width of a rectangle, return area.
    >>> rectangle_area(5, 3)
    15
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""
    return a * b

def circle_area(r):
    """Given radius r, return area of circle.
    >>> circle_area(5)
    78.53981633974483
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""
    from math import pi
    return pi * (r**2)

def sphere_volume(r):
    """Given radius r, return volume of sphere.
    >>> sphere_volume(5)
    523.5987755982989
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""
    from math import pi
    return (4/3) * pi * r**3

def cone_volume(r, h):
    """Given radius r and height h, return volume of cone.
    >>> cone_volume(5, 10)
    113.09733552923254
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""
    from math import pi
    return (1/3) * pi * r**2 * h

def pyramid_volume(b, h):
    """Given base b and height h, return volume of pyramid.
    >>> pyramid_volume(5, 10)
    50
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""
    return (b * h) / 3

def cylinder_volume(r, h):
    """Given radius