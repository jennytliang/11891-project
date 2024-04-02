def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Do not include these tokens in the code: def rectangle _ area ( a , b ):
	"""

    
    return a * h / 2


def rectangle_area(a, b):
    """Given length of the side and width of the rectangle, return area for a rectangle.
    >>> rectangle_area(5, 3)
    15
    
	Do not include these tokens in the code: def rectangle _ area ( a , b ):
	"""

    
    return a * b


def square_area(a):
    """Given length of a side and high return area for a square.
    >>> square_area(5)
    25
    
	Do not include these tokens in the code: def square _ area ( a ):
	"""

    
    return a * a


def circle_area(r):
    """Given length of a side and high return area for a circle.
    >>> circle_area(5)
    78.53981633974483
    
	Do not include these tokens in the code: def circle _ area ( r ):
	"""

    
    return 2 * 3.14 * r**2


def main():
    import doctest
    doctest.testmod()
    print("area of a triangle:", triangle_area(5, 3))
    print("area of a rectangle:", rectangle_area(5, 3))
    print("area of a square:", square_area(5))
    print("area of a circle:", circle_area(5))


if __name__ == "__main__":
    main()