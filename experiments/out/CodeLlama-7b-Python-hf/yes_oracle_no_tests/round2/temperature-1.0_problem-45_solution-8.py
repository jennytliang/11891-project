def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""
    r = a * h / 2
    return r


def rectangle_area(a, b):
    """Given length of a side and high return area for a rectangle.
    >>> rectangle_area(5, 3)
    15
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""
    r = a * b
    return r


def circle_area(r):
    """Given radius return area for a circle.
    >>> circle_area(5)
    78.53981633974483
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""
    r = 3.14 * r * r
    return r


def square_area(a):
    """Given length of a side return area for a square.
    >>> square_area(5)
    25
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""
    r = a * a
    return r


def main():
    import doctest
    doctest.testmod()
    print("""
    Now that you've completed the triangle_area function,
    let's call it in a new function named area.
    Calling a function uses its name followed by parentheses:
    >>> area(5, 3)
    7.5
    """)

    print("""
    Now that you've completed the rectangle_area function,
    let's call it in a new function named area.
    Calling a function uses its name followed by parentheses:
    >>> area(5, 3)
    15
    """)

    print("""
    Now that you've completed the circle_area function,
    let's call it in a new function named area.
    Calling a function uses its name followed by parentheses:
    >>> area(5)
    78.53981633974483
    """)