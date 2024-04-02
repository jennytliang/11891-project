def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Include these tokens in the code: * h /
	"""

    ret = (h * a) / 2
    return ret


def test_triangle_area():
    assert triangle_area(10, 2) == 10
    assert triangle_area(10, 2) != 12
    assert triangle_area(10, 2) != 11
    assert triangle_area(10, 2) != 9


def test_triangle_area_docstring():
    assert triangle_area.__doc__ == "Given length of a side and high return area for a triangle."


def triangle_area_alt(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area_alt(5, 3)
    7.5
    
	Include these tokens in the code: * h /
	"""
    ret = a * h / 2
    return ret


def test_triangle_area_alt():
    assert triangle_area_alt(10, 2) == 10
    assert triangle_area_alt(10, 2) != 12
    assert triangle_area_alt(10, 2) != 11
    assert triangle_area_alt(10, 2) != 9


def test_triangle_area_docstring_alt():
    assert triangle_area_alt.__doc__ == "Given length of a side and high return area for a triangle."


def test_triangle_area_docstring_alt_2():
    assert triangle_area_alt.__doc__ == "Given length of a side and high return area for a triangle."


def test_triangle_area_docstring_alt_3():
    assert triangle_area_alt.__doc__ == "Given length of a side and high return area for a triangle."


def test_triangle_area_docstring_alt_4():
    assert triangle_area_alt.__doc__ == "Given length of a side and high return area for a triangle."


def test_triangle_area_docstring_alt_5():
    assert triangle_area_alt.__doc__ ==