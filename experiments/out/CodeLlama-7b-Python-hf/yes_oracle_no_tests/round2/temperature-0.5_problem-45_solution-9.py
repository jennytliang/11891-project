def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Do not include these tokens in the code: d = { " a ":
	"""


    return a * h / 2



def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(2, 2) == 2.0
    assert triangle_area(7, 1) == 7.0
    assert triangle_area(1, 1) == 0.5
    assert triangle_area(1, 10) == 5.0


if __name__ == "__main__":
    import doctest
    doctest.testmod()
