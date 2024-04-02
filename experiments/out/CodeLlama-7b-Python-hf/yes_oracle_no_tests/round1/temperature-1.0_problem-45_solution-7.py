def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Include these tokens in the code: a
	Do not include these tokens in the code: (
	"""

    r = a * h / 2
    return r

def hexagon_area(side_length):
    """Given side length return area of hexagon.
    >>> hexagon_area(5)
    15.0

	Include these tokens in the code: A

	"""

    A = (6 * pow(side_length, 2)) / (4 * pow(3,0.5))
    return A

def average(x,y):
    """given two numbers, returns their average.
    >>> average(50,50)
    50

	Include these tokens in the code: x,y

	"""
    average = (x+y)/2
    return average

def sum(x,y):
    """given two numbers, returns their sum.
    >>> sum(50,50)
    100

	Include these tokens in the code:
    x
	
	"""
    s = x+y
    return s