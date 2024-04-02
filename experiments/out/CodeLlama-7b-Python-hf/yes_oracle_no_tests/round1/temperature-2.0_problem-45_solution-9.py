def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	"""
    return a * h / 2

def square_area(a):
    """Given length of a side return area for a square.
    >>> square_area(5)
    25
    
	"""
    return a * a

def rectangle_area(a, b):
    """Given length and width of a rectangle return area for a rectangle.
    >>> rectangle_area(5, 3)
    15
    
	"""
    return a * b

def circle_area(r):
    """Given radius of a circle return area for a circle.
    >>> circle_area(5)
    78.53981633974483
    
	"""
    return 3.14 * r * r

def circumference(r):
    """Given radius of a circle return circumference for a circle.
    >>> circumference(5)
    31.41592653589793
    
	"""
    return 2 * 3.14 * r

def sphere_volume(r):
    """Given radius of a sphere return volume for a sphere.
    >>> sphere_volume(5)
    523.5987755982989
    
	"""
    return 4/3 * 3.14 * r * r * r

def sphere_surface_area(r):
    """Given radius of a sphere return surface area for a sphere.
    >>> sphere_surface_area(5)
    160.1024523533546
    
	"""
    return 4 * 3.14 * r * r

def pyramid_volume(b, h):
    """Given base and height return volume for a pyramid.
    >>> pyramid_volume(5, 3)
    15
    
	"""
    return b * h / 3

def pyramid_surface_area(b, h):
    """Given base and height return surface area for