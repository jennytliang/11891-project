def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Do not include these tokens in the code: # code goes here
	"""

    # code goes here
    return a * h / 2.0

if __name__ == '__main__':
    import doctest
    doctest.testmod()