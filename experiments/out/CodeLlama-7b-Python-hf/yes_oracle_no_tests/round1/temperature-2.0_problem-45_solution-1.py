def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Include these tokens in the code: a
	Do not include these tokens in the code: (
	"""

    r = a * h / 2
    return r


def main():
    """Print the area for a triangle with sides of length 5 and 3.
    """
    print(triangle_area(5, 3))
    
    import doctest
    doctest.testmod()  # Run self-test code


if __name__ == "__main__":
    main()