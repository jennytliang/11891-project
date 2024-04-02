def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Include these tokens in the code: return a * h /
	"""
    return a * h / 2

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5

if __name__ == "__main__":
    import doctest
    doctest.testmod()