def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""
    # BEGIN PROBLEM 1
    return a * h / 2
    # END PROBLEM 1


def rectangle_area(a, b):
    """Given length of 2 sides of a rectangle, return area.
    >>> rectangle_area(5, 3)
    15
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""
    # BEGIN PROBLEM 2
    return a * b
    # END PROBLEM 2


def square_area(a):
    """Given length of one side of a square, return area.
    >>> square_area(5)
    25
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""
    # BEGIN PROBLEM 3
    return a * a
    # END PROBLEM 3


def circle_area(r):
    """Given length of a circle's radius, return area.
    >>> circle_area(5)
    78.53981633974483
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""
    # BEGIN PROBLEM 4
    import math
    return math.pi * r * r
    # END PROBLEM 4


def area(a, b, c):
    """Returns the area of a triangle, treating the input values as
    side lengths.
    >>> area(3, 4, 5)
    6.0
    """
    # BEGIN PROBLEM 5
    return triangle_area(a, cathetus(a, b, c)) + triangle_area(b, cathetus(b, a, c)) + triangle_area(c, cathetus(c, a, b))
    # END PROBLEM 5


def cathetus(a, b, c):
    """Return the length of the cathetus that does not