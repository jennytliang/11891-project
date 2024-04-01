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
    """Given length and width return area for a rectangle.
    >>> rectangle_area(5, 3)
    15
    """
    return a * b


def rhombus_area(a, b):
    """Given length of diagonals return area for a rhombus.
    >>> rhombus_area(5, 3)
    7.5
    """
    return a * b / 2


def trapezoid_area(a, b, h):
    """Given lengths of two sides and height return area for a trapezoid.
    >>> trapezoid_area(5, 3, 2)
    9.0
    """
    return (a + b) * h / 2


def regular_polygon_area(perimeter, apothem):
    """Given perimeter and apothem return area for a regular polygon.
    >>> regular_polygon_area(10, 2)
    20.0
    """
    return perimeter * apothem / 2
