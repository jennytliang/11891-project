def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Include these tokens in the code: return a * h /
	"""
    return a * h / 2

def circle_area(r):
    """Given radius of a circle return area for a circle.
    >>> circle_area(5)
    78.53981633974483
    
	Include these tokens in the code: return 3.14 * r ** 2
	"""
    return 3.14 * r ** 2

def rectangle_area(w, h):
    """Given width and high return area for a rectangle.
    >>> rectangle_area(5, 3)
    15
    
	Include these tokens in the code: return w * h
	"""
    return w * h

def square_area(s):
    """Given length of a side return area for a square.
    >>> square_area(5)
    25
    
	Include these tokens in the code: return s ** 2
	"""
    return s ** 2

def test_triangle_area_values():
    assert (triangle_area(10, 5) == 25)
    assert (triangle_area(1, 1) == 0.5)
    assert (triangle_area(2, 2) == 2)
    assert (triangle_area(3, 3) == 27)
    assert (triangle_area(5, 1) == 5)

def test_circle_area_values():
    assert (circle_area(1) == 3.14)
    assert (circle_area(5) == 78.54)
    assert (circle_area(10) == 314.15)
    assert (circle_area(100) == 31415.926535)

def test_rectangle_area_values():
    assert (rectangle_area(1, 1) == 1)
    assert (rectangle_area(10, 1) == 10)
    assert (rectangle_area(1, 10) == 10)
    assert (rectangle_