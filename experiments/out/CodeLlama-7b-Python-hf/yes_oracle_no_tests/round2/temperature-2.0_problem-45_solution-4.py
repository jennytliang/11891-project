def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""
    return a * h / 2


assert triangle_area(5, 3) == 7.5
assert triangle_area(7, 5) == 21
assert triangle_area(3, 5) == 7.5
