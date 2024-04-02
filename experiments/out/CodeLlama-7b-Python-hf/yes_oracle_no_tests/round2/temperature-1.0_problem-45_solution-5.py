def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""

    return (a * h) / 2


def rectangle_area(a, b):
    """Given length of 2 sides return area for a rectangle.
    >>> rectangle_area(5, 3)
    15
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""

    return a * b


def square_area(a):
    """Given length of a side return area for a square.
    >>> square_area(5)
    25
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""

    return a ** 2


def circle_area(r):
    """Given length of a side return area for a circle.
    >>> circle_area(5)
    78.53981633974483
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""

    return 3.14 * (r ** 2)


def main():
    print('Area of a triangle is', triangle_area(5, 3))
    print('Area of a rectangle is', rectangle_area(5, 3))
    print('Area of a square is', square_area(5))
    print('Area of a circle is', circle_area(5))


if __name__ == '__main__':
    main()
