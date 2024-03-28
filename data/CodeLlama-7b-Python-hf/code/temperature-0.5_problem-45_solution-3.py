def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
    return a * h / 2


def rectangle_area(a, b):
    """Given length and width return area for a rectangle.
    >>> rectangle_area(5, 3)
    15
    """
    return a * b


def square_area(a):
    """Given length of side return area for a square.
    >>> square_area(5)
    25
    """
    return a * a


def circle_area(r):
    """Given radius return area for a circle.
    >>> circle_area(5)
    78.53981633974483
    """
    return 3.141592653589793 * r * r


def triangle_perimeter(a, h):
    """Given length of a side and high return perimeter for a triangle.
    >>> triangle_perimeter(5, 3)
    12
    """
    return a * 2 + h


def rectangle_perimeter(a, b):
    """Given length and width return perimeter for a rectangle.
    >>> rectangle_perimeter(5, 3)
    16
    """
    return a * 2 + b * 2


def square_perimeter(a):
    """Given length of side return perimeter for a square.
    >>> square_perimeter(5)
    20
    """
    return a * 4


def circle_perimeter(r):
    """Given radius return perimeter for a circle.
    >>> circle_perimeter(5)
    31.41592653589793
    """
    return 2 * 3.141592653589793 * r


def triangle_diameter(a, h):
    """Given length of a side and high return diameter for a triangle.
    >>> triangle_diameter(5, 3)
    7.0710678118654755
    """
    return (a * a + h * h) ** 0.5


def rectangle_diameter(a, b):
    """Given length and width return diameter for a rectangle.
    >>> rectangle_diameter(5, 3)
    7.0710678118654755
    """
    return (a * a + b * b) ** 0.5


def square_diameter(a):
    """Given length of side return diameter for a square.
    >>> square_diameter(5)
    7.0710678118654755
    """
    return (2 * a * a) ** 0.5


def circle_diameter(r):
    """Given radius return diameter for a circle.
    >>> circle_diameter(5)
    10
    """
    return 2 * r


def triangle_circumradius(a, h):
    """Given length of a side and high return circumradius for a triangle.
    >>> triangle_circumradius(5, 3)
    3.5355339059327373
    """
    return (a * a + h * h) ** 0.5 / 2


def rectangle_circumradius(a, b):
    """Given length and width return circumradius for a rectangle.
    >>> rectangle_circumradius(5, 3)
    3.5355339059327373
    """
    return (a * a + b * b) ** 0.5 / 2


def square_circumradius(a):
    """Given length of side return circumradius for a square.
    >>> square_circumradius(5)
    3.5355339059327373
    """
    return (2 * a * a) ** 0.5 / 2


def circle_circumradius(r):
    """Given radius return circum