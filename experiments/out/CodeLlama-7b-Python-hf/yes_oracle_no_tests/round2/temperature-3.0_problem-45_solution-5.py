def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""
    r = a * h / 2
    return r


def rectangle_area(l, w):
    """Given length and width return area for a rectangle.
    >>> rectangle_area(3, 5)
    15
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""
    r = l * w
    return r


def circle_area(r):
    """Given radius of a circle return area for a circle.
    >>> circle_area(3)
    28.274333882308138
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""
    r = 3.14 * r ** 2
    return r


def cube_volume(a):
    """Given length of a side return volume for a cube.
    >>> cube_volume(3)
    27
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""
    r = a ** 3
    return r


def sphere_volume(r):
    """Given radius of a sphere return volume for a sphere.
    >>> sphere_volume(3)
    523.5987755982989
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""
    r = 4 / 3 * 3.14 * r ** 3
    return r


def average_volume(a, b):
    """Given length of a side for a cube and radius of a sphere
    return average of volume for a cube and a sphere.
    >>> average_volume(3, 3)
    29.166666666666668
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""
    r = (sphere_volume(a) + cube_volume