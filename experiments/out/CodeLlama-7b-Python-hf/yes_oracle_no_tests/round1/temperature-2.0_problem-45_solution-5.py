def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Include these tokens in the code: a
	Do not include these tokens in the code: (
	"""

    r = a * h / 2
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

def rectangle_area(a, b):
    """Given length and width of a rectangle, return area.
    >>> rectangle_area(5, 3)
    15
    
	Include these tokens in the code: a, b
	Do not include these tokens in the code: (
	"""

    r = a * b
    return r

def circle_area(r):
    """Given length of a side return area for a circle.
    >>> circle_area(5)
    78.53981633974483
    
	Include these tokens in the code: r
	Do not include these tokens in the code: (
	"""

    r = pi * r * r
    return r

#print(triangle_area(5, 3))
#print(square_area(5))
#print(rectangle_area(5, 3))
#print(circle_area(5))



def area_of_shape(a, h, b, r):
    """Given length of a side and high return area for a triangle.
    >>> area_of_shape(5, 3)
    7.5
    
	Include these tokens in the code: a
	Do not include these tokens in the code: (
	"""

    if a != None:
        r = triangle_area(a, h)
    elif b != None and r != None:
        r = rectangle_area(b, r)
    elif a != None and b != None:
        r = square_area(a)
    elif r != None:
        r = circle_area(r)
    return r

#print(area_of_shape(5, 3))
#