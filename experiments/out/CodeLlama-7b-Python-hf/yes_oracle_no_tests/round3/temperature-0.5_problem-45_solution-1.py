def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Do not include these tokens in the code: def main (): print (" Enter the length
	"""



    return a * 1.0 / 2 * h

def f(x):
    """Given x return x^2"""
    return x * x

def g(x):
    """Given x return x^3"""
    return x * x * x

def h(x):
    """Given x return x^4"""
    return x * x * x * x

def area_of_polygon(sides, length_of_sides):
    """Given sides and length of sides return area of a polygon"""
    s = 0
    for i in range(sides):
        s += triangle_area(length_of_sides, length_of_sides)
    return s

def main():
    print("Area of a triangle is ", triangle_area(5, 3))
    print("5^2 is ", f(5))
    print("5^3 is ", g(5))
    print("5^4 is ", h(5))
    print("Area of a regular pentagon is ", area_of_polygon(5, 3))
    print("Area of a regular hexagon is ", area_of_polygon(6, 3))
    print("Area of a regular heptagon is ", area_of_polygon(7, 3))
    print("Area of a regular octagon is ", area_of_polygon(8, 3))
    print("Area of a regular nonagon is ", area_of_polygon(9, 3))
    print("Area of a regular decagon is ", area_of_polygon(10, 3))

if __name__ == "__main__":
    import doctest
    doctest.testmod()