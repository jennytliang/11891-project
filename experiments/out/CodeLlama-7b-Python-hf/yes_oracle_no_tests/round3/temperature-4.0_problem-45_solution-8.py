def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Do not include these tokens in the code: def main (): print (" Area of
	"""


    return a * h / 2

def rectangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> rectangle_area(5, 3)
    15
    
	Do not include these tokens in the code: def main (): print (" Area of
	"""


    return a * h

def circle_area(r):
    """Given radius r return area for a circle.
    >>> circle_area(5)
    78.53981633974483
    
	Do not include these tokens in the code: def main (): print (" Area of
	"""


    return 3.14 * r ** 2

def sphere_area(r):
    """Given radius r return area for a sphere.
    >>> sphere_area(5)
    523.5987755982989
    
	Do not include these tokens in the code: def main (): print (" Area of
	"""


    return 4 * 3.14 * r ** 2

def cone_area(r, h):
    """Given radius r and high return area for a cone.
    >>> cone_area(5, 3)
    61.31876544337979
    
	Do not include these tokens in the code: def main (): print (" Area of
	"""


    return 3.14 * r * (r + h)

def cylinder_area(r, h):
    """Given radius r and high return area for a cylinder.
    >>> cylinder_area(5, 3)
    167.46902215556798
    
	Do not include these tokens in the code: def main (): print (" Area of
	"""


    return 2 * 3.14 * r * h

def pyramid_area(b, h):
    """Given base b and high return area for a pyramid.
    >>> py