def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Do not include these tokens in the code: def test _ triangle _ area (): assert
	"""

    return a * h  # remove this line


def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(1, 1) == 0.5
    assert triangle_area(10, 10) == 50
    assert triangle_area(1, 100) == 50


if __name__ == "__main__":
    test_triangle_area()
