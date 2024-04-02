def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""
    # Insert your code here.
    return a * h / 2


print(triangle_area(5, 3))


def circle_area(r):
    """Given radius return area for a circle.
    >>> circle_area(5)
    78.5398163397
    """
    # Insert your code here.
    return 3.142 * r * r


print(circle_area(5))


def rectangle_area(a, b):
    """Given length of a side and high return area for a rectangle.
    >>> rectangle_area(5, 3)
    15
    """
    # Insert your code here.
    return a * b


print(rectangle_area(5, 3))


def square_area(a):
    """Given length of a side return area for a square.
    >>> square_area(5)
    25
    """
    # Insert your code here.
    return a * a


print(square_area(5))
