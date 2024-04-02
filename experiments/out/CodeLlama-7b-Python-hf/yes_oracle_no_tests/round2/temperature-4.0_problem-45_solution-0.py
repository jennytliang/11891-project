def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Do not include these tokens in the code: # return a * h /
	"""
    return a * h / 2.0


def main():
    import doctest

    doctest.testmod()  # Run all doctests in the module

    # Uncomment and comment out the following lines to test your function
    # print(triangle_area(3, 2))
    # print(triangle_area(5, 3))


if __name__ == '__main__':
    main()