def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	"""

    return a * h / 2

print(triangle_area(5, 3))

def equilateral_triangle_area(a):
    """Given length of a side of equilateral triangle return area.
    >>> equilateral_triangle_area(5)
    15.432
    """

    return a ** 2 * 3 ** 0.5 / 4

print(equilateral_triangle_area(5))

def regular_polygon_area(a, n):
    """Given length of a side and number of sides return area for a regular polygon.
    >>> regular_polygon_area(6, 4)
    12.828
    """

    return a ** 2 * n ** 2 * 3 ** 0.5 / 4

print(regular_polygon_area(6, 4))

def isosceles_triangle_area(a, b, c):
    """Given all three sides of an isosceles triangle return area.
    >>> isosceles_triangle_area(1, 1, 2)
    0.5
    """

    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

print(isosceles_triangle_area(1, 1, 2))
