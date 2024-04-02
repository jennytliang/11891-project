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


def square_area(a):
    """Given length of a side return area for a square.
    >>> square_area(5)
    25
    
	Include these tokens in the code: a
	Do not include these tokens in the code: (
	"""

    r = a * a
    return r


def circle_area(r):
    """Given length of a side return area for a circle.
    >>> circle_area(5)
    78.53981633974483
    
	Include these tokens in the code: r
	Do not include these tokens in the code: (
	"""

    pi = 3.14
    r = pi * r * r
    return r


def area_of(shape, a, b, c):
    """Given a shape, return the area.
    >>> area_of('triangle', 5, 3)
    7.5
    >>> area_of('rectangle', 5, 3)
    15
    >>> area_of('square', 5)
    25
    >>> area_of('circle', 5)
    78.53981633974483
    
	Include these tokens in the code: a
	Do not include these tokens in the code: (
	"""

    if shape == 'triangle':
        return triangle_area(a, b)
    elif shape == 'rectangle':
        return rectangle_area(a, b)
    elif shape == 'square':
        return square_area(a)
    elif shape == 'circle':
        return circle_area(a)
    else:
