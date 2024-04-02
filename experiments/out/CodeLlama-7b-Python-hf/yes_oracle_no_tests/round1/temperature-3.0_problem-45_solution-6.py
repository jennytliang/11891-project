def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Include these tokens in the code: a
	Do not include these tokens in the code: (
	"""

    r = a*h/2
    return r

def triangle_area_2(b, c):
    """Given length of two sides return area for a triangle.
    >>> triangle_area_2(5, 3)
    7.5
    
	Include these tokens in the code: a
	Do not include these tokens in the code: (
	"""

    r = (b+c)/2
    return r

def main():
    import doctest
    doctest.testmod()
    a = float(input("Length of a side:"))
    h = float(input("Height:"))
    print("Area:", triangle_area(a, h))

if __name__ == "__main__":
    main()
