def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""
    # YOUR CODE HERE
    return 0.5 * a * h

def rectangle_area(width, height):
    """Given width and height return area for a rectangle.
    >>> rectangle_area(5, 3)
    15
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""
    # YOUR CODE HERE
    return width * height

def square_area(side):
    """Given side return area for a square.
    >>> square_area(5)
    25
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""
    # YOUR CODE HERE
    return side * side

def circle_area(radius):
    """Given radius return area for a circle.
    >>> circle_area(5)
    78.53981633974483
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""
    # YOUR CODE HERE
    import math
    return math.pi * radius * radius

def triangle_area_alt(a, h):
    """Given length of a side and high return area for a triangle.
    >>> circle_area(5)
    78.53981633974483
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""
    # YOUR CODE HERE
    return a * h / 2

def rectangle_area_alt(width, height):
    """Given width and height return area for a rectangle.
    >>> rectangle_area(5, 3)
    15
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""
    # YOUR CODE HERE
    return width * height

def square_area_alt(side):
    """Given side return area for a square.
   