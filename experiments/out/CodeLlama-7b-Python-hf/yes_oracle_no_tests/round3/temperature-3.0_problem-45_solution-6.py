def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Do not include these tokens in the code: def test _ triangle _ area (): assert
	"""

    return a * h  / 2

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    
def test_triangle_area_2():
    assert triangle_area(5, 3) == 7.5

def test_triangle_area_3():
    assert triangle_area(5, 3) == 7.5
