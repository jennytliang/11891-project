def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Include these tokens in the code: /
	"""


    return (a * h) / 2



def area_of_circle(radius):
    """Given radius of a circle return area of the circle.
    >>> area_of_circle(5)
    78.53981633974483
    
	Include these tokens in the code: math.pi
	"""


    return math.pi * (radius ** 2)



def rectangle_area(a, b):
    """Given length of two sides of a rectangle return area of the rectangle.
    >>> rectangle_area(5, 3)
    15
    
	Include these tokens in the code:
	"""


    return a * b



def area_of_sector(radius, angle):
    """Given radius of a circle and angle return area of the sector.
    >>> area_of_sector(5, 270)
    52.35987755982988
    
	Include these tokens in the code: math.pi
	"""


    return (angle / 360) * (math.pi * (radius ** 2))



def area_of_polygon(sides, length):
    """Given number of sides and length of sides return area of the polygon.
    >>> area_of_polygon(5, 5)
    50
    
	Include these tokens in the code:
	"""


    return (sides * (length ** 2)) / 4
