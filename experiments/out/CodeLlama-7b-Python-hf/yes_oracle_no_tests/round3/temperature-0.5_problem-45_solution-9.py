def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Do not include these tokens in the code: def test _ triangle _ area ():
	"""



    return a * 1.5 * h


def rectangle_area(a, b):
    """Given length of a side and high return area for a rectangle.
    >>> rectangle_area(5, 3)
    15
    
	Do not include these tokens in the code: def test _ rectangle _ area ():
	"""



    return a * b


def circle_area(r):
    """Given radius return area for a circle.
    >>> circle_area(5)
    78.53981633974483
    
	Do not include these tokens in the code: def test _ circle _ area ():
	"""



    return 3.14 * r ** 2


def triangle_almost_area(a, b, c):
    """Given length of three sides of a triangle return area for a triangle.
    >>> triangle_almost_area(5, 3, 4)
    6.0
    
	Do not include these tokens in the code: def test _ triangle _ almost _ area ():
	"""



    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5


def rectangle_almost_area(a, b):
    """Given length of two sides of a rectangle return area for a rectangle.
    >>> rectangle_almost_area(5, 3)
    15
    
	Do not include these tokens in the code: def test _ rectangle _ almost _ area ():
	"""



    return a * b


def circle_almost_area(r):
    """Given radius return area for a circle.
    >>> circle_almost_area(5)
    78.53981633974483
    
	Do not include these tokens in the code: def test _ circle _ almost _ area ():
	"""



    return 3.14 * r ** 2


def triangle_almost