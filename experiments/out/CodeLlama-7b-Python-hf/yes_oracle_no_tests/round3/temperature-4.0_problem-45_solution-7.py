def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Do not include these tokens in the code: print ( triangle _ area ( 5 , 3
	"""


    return a * h / 2


def rectangle_area(a, b):
    """Given length of a side and high return area for a rectangle.
    >>> rectangle_area(5, 3)
    15
    
	Do not include these tokens in the code: print ( rectangle _ area ( 5 , 3
	"""


    return a * b


def square_area(a):
    """Given length of a side and high return area for a square.
    >>> square_area(5)
    25
    
	Do not include these tokens in the code: print ( square _ area ( 5
	"""


    return a ** 2


def circle_area(r):
    """Given length of a side and high return area for a circle.
    >>> circle_area(5)
    78.53981633974483
    
	Do not include these tokens in the code: print ( circle _ area ( 5
	"""


    return 3.14159265359 * r ** 2


def kite_area(a, b, c):
    """Given length of a side and high return area for a kite.
    >>> kite_area(5, 5, 5)
    50
    
	Do not include these tokens in the code: print ( kite _ area ( 5 , 5 , 5
	"""


    return a * b * c / 2


def main():
    print("You are using the triangle_area function")
    print("The area of the triangle is: ", triangle_area(5, 3))
    print("You are using the rectangle_area function")
    print("The area of the rectangle is: ", rectangle_area(5, 3))
    print("You are using the square_area function")
    print("The area of the square is: ", square_area(5))
    print("You are using the circle_area function")
    print("The area of the circle is: ", circle_area(5))
    print("