def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Include these tokens in the code: /
	"""


    return a*h/2


assert triangle_area(5, 3) == 7.5
assert triangle_area(1, 10) == 5.0
assert triangle_area(10, 1) == 5.0
assert triangle_area(1, 1) == 0.5
assert triangle_area(5, 6) == 15.0
assert triangle_area(10, 2) == 10.0
assert triangle_area(2, 10) == 10.0
assert triangle_area(10, 10) == 50.0
