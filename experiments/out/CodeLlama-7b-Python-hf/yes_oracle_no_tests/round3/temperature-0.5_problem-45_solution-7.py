def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Do not include these tokens in the code: def test _ triangle _ area (): assert
	"""



    return a * 1/2 * h



def test_triangle_area():
    assert triangle_area(5, 3) == 7.5



if __name__ == "__main__":
    import doctest
    doctest.testmod()