def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Do not include these tokens in the code: def rectangle _ area ( a , b ):
	"""

    return a * h / 2


d = {
    'a': 5,
    'b': 3,
}

print(triangle_area(**d))
