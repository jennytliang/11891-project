def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Include these tokens in the code: return a * h /
	"""
    return a * h / 2


def circle_area(r):
    """Given radius of a circle return area for a circle.
    >>> circle_area(5)
    78.53981633974483
    
	Include these tokens in the code: return 3.14159 * r ** 2
    """
    return 3.14159 * r ** 2


def trapezoid_area(a, b, h):
    """Given two sides and high return area for a trapezoid.
    >>> trapezoid_area(3, 4, 5)
    10.5
    
	Include these tokens in the code: return (a + b) * h / 2
    """
    return (a + b) * h / 2


def regular_polygon_area(n, side):
    """Given number of sides and side length return area for a regular polygon.
    >>> regular_polygon_area(4, 4)
    10.760644362991673
    
	Include these tokens in the code: return 1 / 4 * n * side ** 2
    """
    return 1 / 4 * n * side ** 2


def sphere_surface_area(r):
    """Given radius of a sphere return surface area for a sphere.
    >>> sphere_surface_area(5)
    314.1592653589793
    
	Include these tokens in the code: return 4 * 3.14159 * r ** 2
    """
    return 4 * 3.14159 * r ** 2


def sphere_volume(r):
    """Given radius of a sphere return volume for a sphere.
    >>> sphere_volume(5)
    523.5987755982989
    
	Include these tokens in the code: return 4 / 3 * 3.1415