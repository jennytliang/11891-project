def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Do not include these tokens in the code: print ( triangle _ area ( 5 , 3
	"""


    return a * h / 2


def area_of_square(a):
    """Given length of a side return area for a square.
    >>> area_of_square(5)
    25
    """
    return a * a


def area_of_rectangle(a, b):
    """Given lengths of two sides of a rectangle return its area.
    >>> area_of_rectangle(5, 3)
    15
    """
    return a * b


def area_of_triangle_by_three_sides(a, b, c):
    """Given lengths of 3 sides of a triangle return its area.
    >>> area_of_triangle_by_three_sides(5, 3, 4)
    6.0
    """
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


def area_of_parallelogram(a, h):
    """Given length of a side and high return area for a parallelogram.
    >>> area_of_parallelogram(5, 3)
    15
    """
    return a * h


def area_of_trapezium(a, b, h):
    """Given lengths of 2 sides and high return area for a trapezium.
    >>> area_of_trapezium(5, 3, 4)
    19.0
    """
    return 1 / 2 * (a + b) * h


def area_of_sector(r, theta):
    """Given radius and central angle in degrees return area of sector.
    >>> area_of_sector(5, 30)
    1.5707963267948966
    """
    return r ** 2 * theta / 2 * (180 / math.pi)


def area_of_circle(r):
    """Given radius return area of circle.
    >>> area_of_