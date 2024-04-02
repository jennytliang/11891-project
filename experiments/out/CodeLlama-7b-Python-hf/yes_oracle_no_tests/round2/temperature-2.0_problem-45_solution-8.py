def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Do not include these tokens in the code: print ( triangle _ area ( 5 , 3
	"""


    return a * h / 2





def quadrilateral_area(a, b, c, d):
    """Given length of 4 sides return area for a quadrilateral.
    >>> quadrilateral_area(5, 3, 3, 4)
    10.5
    
	Do not include these tokens in the code: print ( quadrilateral _ area ( 5 , 3 , 3 , 4
	"""


    return triangle_area(a, d) + triangle_area(b, c)





def rectangle_area(a, b):
    """Given length of 2 sides return area for a rectangle.
    >>> rectangle_area(5, 3)
    15
    
	Do not include these tokens in the code: print ( rectangle _ area ( 5 , 3
	"""


    return a * b





def square_area(a):
    """Given length of 1 side return area for a square.
    >>> square_area(5)
    25
    
	Do not include these tokens in the code: print ( square _ area ( 5
	"""


    return a * a





def rhombus_area(a, h):
    """Given length of diagonals return area for a rhombus.
    >>> rhombus_area(5, 3)
    15
    
	Do not include these tokens in the code: print ( rhombus _ area ( 5 , 3
	"""


    return triangle_area(a, h) + triangle_area(a, h)





def parallelogram_area(a, h):
    """Given length of base and height return area for a parallelogram.
    >>> parallelogram_area(5, 3)
    15
    
	Do not include these tokens in the code: print ( parallelogram _ area ( 5 , 3
	"""


    return a * h





def trapezoid_