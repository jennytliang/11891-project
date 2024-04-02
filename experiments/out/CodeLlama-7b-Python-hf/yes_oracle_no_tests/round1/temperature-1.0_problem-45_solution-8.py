def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Include these tokens in the code: a
	Do not include these tokens in the code: (
	"""

    r = h*a/2
    return r


def circle_area(r):
    """Given radius of a circle return area for a circle.
    >>> circle_area(20)
    1256.6370614359173
    >>> circle_area(math.sqrt(2))
    1.5707963267948966
   
	Include these tokens in the code: 2, math, math., pi
	Do not include these tokens in the code: r, pi, radius
    """

    import math
    area = math.pi*(r**2)
    return area


def quadrilateral_area(a, b, c, d):
    """Given lengths of 4 sides of a quadrilateral return area for it.
    >>> quadrilateral_area(2, 2, 2, 2)
    1.0
    >>> quadrilateral_area(2, 3, 4, 5)
    6.0
	
	Include these tokens in the code: c
    Do not include these tokens in the code: l, a, b, d, ...
    """

    r = a * b + b * c + c * d + d * a
    return r


def is_triangle(a, b, c):
    """Given lengths of 3 sides of a potential triangle return whether it is
    actually a triangle.
    """
    if a > b and a > c and a > b+c:
        return True
    elif b > a and b > c and b > a+c:
        return True
    elif c > b and c > a and c > b+a:
        return True
    elif a+b < c or b+c < a or c+a < b:
        return True
    else:
        return False
