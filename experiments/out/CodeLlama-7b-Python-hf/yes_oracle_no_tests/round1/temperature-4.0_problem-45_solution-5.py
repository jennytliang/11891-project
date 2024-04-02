def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Include these tokens in the code: return a * h /
	"""
    return a * h / 2

def circle_area(r):
    """Given length of a side and high return area for a circle.
    >>> circle_area(5)
    78.53981633974483
    
	Include these tokens in the code: return 3.14 * r ** 2
	"""
    return 3.14 * r ** 2

def is_right(a, b, c):
    """Given three side lengths of a triangle, return True if the
    triangle is right and False otherwise.
    
    Note: the sides must be given in order from smallest to largest.
    
    >>> is_right(1, 2, 5)
    True
    >>> is_right(3, 4, 5)
    False
    >>> is_right(5, 4, 3)
    False
    """
    return (a ** 2 + b ** 2) == c ** 2

def is_equilateral(a, b, c):
    """Given three side lengths of a triangle, return True if the
    triangle is equilateral and False otherwise.
    
    Note: the sides must be given in order from smallest to largest.
    
    >>> is_equilateral(1, 1, 1)
    True
    >>> is_equilateral(1, 2, 2)
    False
    >>> is_equilateral(2, 2, 2)
    True
    """
    return a == b == c

def is_isosceles(a, b, c):
    """Given three side lengths of a triangle, return True if the
    triangle is isosceles and False otherwise.
    
    Note: the sides must be given in order from smallest to largest.
    
    >>> is_isosceles(1, 2, 2)
    True
    >>> is_isosceles(1, 2, 3)
    False
    >>> is_isosceles(2, 2, 3)
    False