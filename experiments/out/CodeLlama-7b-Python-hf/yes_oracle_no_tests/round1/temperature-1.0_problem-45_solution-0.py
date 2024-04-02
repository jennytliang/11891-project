def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Include these tokens in the code: a
	Do not include these tokens in the code: (
	"""

    r = a * h / 2
    return r

def triangle_area_alt(a, b, c):
    """Given length of three sides return area for a triangle.
    >>> triangle_area_alt(3, 4, 5)
    6.0
    """

    s = (a + b + c) / 2
    r = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return r


def rectangle_area(a, b):
    """Given length of two sides return area for a rectangle.
    >>> rectangle_area(5, 3)
    15
    """

    return a * b

def rectangle_area_alt(a, b):
    """Given length of two sides return area for a rectangle.
    >>> rectangle_area_alt(5, 3)
    15
    """

    return a * b


def square_area(a):
    """Given length of a side return area for a square.
    >>> square_area(5)
    25
    """

    return a ** 2

def square_area_alt(a):
    """Given length of a side return area for a square.
    >>> square_area_alt(5)
    25
    """

    return a ** 2

def rhombus_area(a, h):
    """Given length of diagonals and high return area for a rhombus.
    >>> rhombus_area(5, 3)
    15
    """

    return (a * h) / 2

def rhombus_area_alt(a, b):
    """Given length of diagonals return area for a rhombus.
    >>> rhombus_area_alt(5, 3)
    15
    """

    return (a * b) / 2

def parallelogram_area(a, h):
    """Given length of base and high return area for a parallelogram.
    >>> parallelogram_area