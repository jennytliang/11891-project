def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Do not include these tokens in the code: # Y OUR CO DE H ERE
	"""
    return a * h / 2


def is_triangle(a, b, c):
    """Given three lengths it returns True if it is possible
    to make a triangle with them.
    >>> is_triangle(1, 2, 2)
    True
    >>> is_triangle(1, 2, 3)
    False
    
	Do not include these tokens in the code: # Y OUR CO DE H ERE
	"""
    return a + b > c and a + c > b and b + c > a


def is_right(a, b, c):
    """Given three lengths it returns True if it is possible
    to make a triangle with them and if it is right.
    >>> is_right(3, 4, 5)
    False
    >>> is_right(3, 4, 4)
    False
    >>> is_right(3, 3, 3)
    True
    
	Do not include these tokens in the code: # Y OUR CO DE H ERE
	"""
    return is_triangle(a, b, c) and a * a + b * b == c * c


def equilateral(a, b, c):
    """Given three lengths it returns True if it is possible
    to make a triangle with them and if it is equilateral.
    >>> equilateral(1, 1, 1)
    True
    >>> equilateral(1, 2, 1)
    False
    
	Do not include these tokens in the code: # Y OUR CO DE H ERE
	"""
    return is_triangle(a, b, c) and a == b == c


def isosceles(a, b, c):
    """Given three lengths it returns True if it is possible
    to make a triangle with them and if it is isosceles.
    >>> isosceles(2, 2, 3)
    True
    >>> isosceles(2, 3, 2)
    True
    >>> isosceles(3, 2,