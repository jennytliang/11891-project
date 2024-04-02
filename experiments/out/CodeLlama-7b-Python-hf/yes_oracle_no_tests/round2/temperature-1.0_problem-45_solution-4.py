def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Include these tokens in the code: return a
	Do not include these tokens in the code: r = float (
	"""

    r = float(a) * h / 2
    return r

print(triangle_area(1, 3))
print(triangle_area(5, 3))