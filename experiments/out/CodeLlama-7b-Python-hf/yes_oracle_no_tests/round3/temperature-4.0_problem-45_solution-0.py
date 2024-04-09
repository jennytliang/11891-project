def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Do not include these tokens in the code: . 0
	"""

    return a * 0.5 * h

def area_of_circle(radius):
    """Given radius of a circle, return its area.
    >>> area_of_circle(5)
    78.53981633974483
    
	Do not include these tokens in the code: . 0
	"""

    return 3.14 * radius ** 2


def area_of_rectangle(a, b):
    """Given length of two sides of a rectangle, return its area.
    >>> area_of_rectangle(5, 3)
    15
    
	Do not include these tokens in the code: . 0
	"""

    return a * b


def area_of_sector(radius, angle):
    """Given radius and angle of a sector, return its area.
    >>> area_of_sector(5, 3)
    19.634954084936208
    
	Do not include these tokens in the code: . 0
	"""

    return 0.5 * radius ** 2 * angle


def area_of_triangle_alt(a, b, c):
    """Given lengths of 3 sides of a triangle, return its area.
    >>> area_of_triangle_alt(3, 4, 5)
    6.0
    
	Do not include these tokens in the code: . 0
	"""

    return 0.5 * a * b * (c ** 2)


def area_of_triangle_heron(a, b, c):
    """Given lengths of 3 sides of a triangle, return its area.
    >>> area_of_triangle_heron(3, 4, 5)
    6.0
    
	Do not include these tokens in the code: . 0
	"""

    p = (a + b + c) * 0.5
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5
