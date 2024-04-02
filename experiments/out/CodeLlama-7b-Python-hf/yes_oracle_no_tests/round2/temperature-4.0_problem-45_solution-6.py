def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Do not include these tokens in the code: print ( triangle _ area ( 5 ,
	"""

    return a * h 


def triangle_area_alt(a, b, c):
    """Given three sides of a triangle, return area for a triangle.
    >>> triangle_area_alt(5, 3, 4)
    6
    """
    s = (a + b + c) / 2
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    return area


def triangle_area_alt2(a, b, c):
    """Given three sides of a triangle, return area for a triangle.
    >>> triangle_area_alt2(5, 3, 4)
    6
    """
    s = (a + b + c) / 2
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    return area


def triangle_area_alt3(a, b, c):
    """Given three sides of a triangle, return area for a triangle.
    >>> triangle_area_alt3(5, 3, 4)
    6
    """
    s = (a + b + c) / 2
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    return area


def right_triangles_for_area(area):
    """Given area of a triangle, return all possible triplets of sides.
    >>> right_triangles_for_area(3)
    [(1, 1, 1)]
    >>> right_triangles_for_area(5)
    [(1, 1, 3), (3, 3, 3)]
    """
    result = []
    for a in range(1, area+1):
        for b in range(1, area+1):
            c = area - a - b
            if c >= b:
                result.append((a, b, c))
    return result


def right_triangles_for_area_alt(area):
    """Given area of a triangle, return all possible triplets of sides.
    >>>