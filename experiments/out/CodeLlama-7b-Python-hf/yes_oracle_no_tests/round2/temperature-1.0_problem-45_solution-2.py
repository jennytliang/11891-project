def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""
    return (a * h) / 2


def rectangle_area(a, b):
    """Given length and width return area for a rectangle.
    >>> rectangle_area(5, 3)
    15
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""
    return a * b


def circle_area(r):
    """Given the radius return the area for a circle.
    >>> circle_area(5)
    78.53981633974483
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""
    return 3.14159 * r ** 2


def main():
    print('Triangle, rectangle, or circle?')
    print('(T)riangle, (R)ectangle, or (C)ircle')
    shape = input('Shape: ').upper()

    if shape == 'T':
        print('Enter length of a side, and the height')
        length = float(input('Length: '))
        height = float(input('Height: '))
        print('The area of your triangle is ' + str(triangle_area(length, height)))
    elif shape == 'R':
        print('Enter length and width')
        length = float(input('Length: '))
        width = float(input('Width: '))
        print('The area of your rectangle is ' + str(rectangle_area(length, width)))
    elif shape == 'C':
        print('Enter the radius')
        radius = float(input('Radius: '))
        print('The area of your circle is ' + str(circle_area(radius)))
    else:
        print('That is not a valid shape.')


if __name__ == '__main__':
    main()