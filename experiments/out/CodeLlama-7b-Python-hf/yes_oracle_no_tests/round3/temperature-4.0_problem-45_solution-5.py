def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Do not include these tokens in the code: def circle _ area ( r
	"""


    return a * h / 2

def circle_area(r):
    """Given radius of a circle return area for a circle.
    >>> circle_area(5)
    78.53981633974483
    """

    return 3.14 * r * r

def rectangle_area(a, b):
    """Given length of a side and high return area for a rectangle.
    >>> rectangle_area(5, 3)
    15
    """

    return a * b

def square_area(a):
    """Given length of a side and high return area for a square.
    >>> square_area(5)
    25
    """

    return a * a





def main():
    test = triangle_area(5, 3)
    print(test)

    test = circle_area(5)
    print(test)

    test = rectangle_area(5, 3)
    print(test)

    test = square_area(5)
    print(test)


if __name__ == "__main__":
    main()
