def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Include these tokens in the code: a
	Do not include these tokens in the code: (
	"""

    r = a * h / 2
    return r


def rectangle_area(a, b):
    """Given length of a side and high return area for a rectangle.
    >>> rectangle_area(5, 3)
    15
    
	Include these tokens in the code: a
	Do not include these tokens in the code: (
	"""

    r = a * b
    return r


def circle_area(r):
    """Given radius of a circle return area for a circle.
    >>> circle_area(5)
    78.53981633974483
    
	Include these tokens in the code: r
	Do not include these tokens in the code: (
	"""

    r = 3.14 * r ** 2
    return r


def square_area(a):
    """Given length of a side return area for a square.
    >>> square_area(5)
    25
    
	Include these tokens in the code: a
	Do not include these tokens in the code: (
	"""

    r = a ** 2
    return r


def triangle_perimeter(a, b, c):
    """Given length of a side and high return perimeter for a triangle.
    >>> triangle_perimeter(5, 3, 4)
    14
    
	Include these tokens in the code: a
	Do not include these tokens in the code: (
	"""

    r = a + b + c
    return r


def rectangle_perimeter(a, b):
    """Given length of a side and high return perimeter for a rectangle.
    >>> rectangle_perimeter(5, 3)
    16
    
	Include these tokens in the code: a
	Do not include these tokens in the code: (
	"""

    r = 2 * a + 2 * b
    return r


def circle_perimeter(r):
    """Given radius of a circle return perimeter for a circle.
    >>> circle_perimeter(5