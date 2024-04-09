def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Do not include these tokens in the code: assert triangle _ area ( 5 , 3
	"""

    return a * h  / 2


def triangle_area_2_sides(a, b):
    """Given two sides of a triangle, find the length of the third side and return the area for the triangle.
    >>> triangle_area_2_sides(3, 4)
    4.0
    """

    return (a * b) / 2


def triangle_area_3_sides(a, b, c):
    """Given three sides of a triangle, check if they can form a triangle. If so, find the length of the missing side and return the area for the triangle.
    >>> triangle_area_3_sides(1, 2, 2)
    False
    """

    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    if area > 0:
        return area
    else:
        return False


def is_right(a, b, c):
    """Given three sides of a triangle, check if they can form a right triangle.
    >>> is_right(3, 4, 5)
    True
    """

    if a ** 2 + b ** 2 == c ** 2:
        return True
    else:
        return False
