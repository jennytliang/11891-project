def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Include these tokens in the code: return a * h /
	"""
    return a * h / 2

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(1, 1) == 0.5
    assert triangle_area(10, 10) == 50

def test_triangle_area_error():
    try:
        triangle_area(10, 0)
    except ZeroDivisionError:
        pass
    else:
        assert False

def test_triangle_area_type_error():
    try:
        triangle_area(10, 'a')
    except TypeError:
        pass
    else:
        assert False

def test_triangle_area_value_error():
    try:
        triangle_area(10, -1)
    except ValueError:
        pass
    else:
        assert False

