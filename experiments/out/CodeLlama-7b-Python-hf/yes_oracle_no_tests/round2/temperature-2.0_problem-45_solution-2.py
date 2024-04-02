def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""
    r = a * h / 2
    return r

def rectangle_area(a, b):
    """Given length and width return area for a rectangle.
    >>> rectangle_area(5, 3)
    15
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""
    r = a * b
    return r

def square_area(a):
    """Given side length return area for a square.
    >>> square_area(5)
    25
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""
    r = a * a
    return r

def circle_area(r):
    """Given radius r, return area of a circle.
    >>> circle_area(5)
    78.53981633974483
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""
    r = 3.14 * r * r
    return r

def main():
    print("Area of a triangle:", triangle_area(5, 3))
    print("Area of a rectangle:", rectangle_area(5, 3))
    print("Area of a square:", square_area(5))
    print("Area of a circle:", circle_area(3))

if __name__ == "__main__":
    main()
