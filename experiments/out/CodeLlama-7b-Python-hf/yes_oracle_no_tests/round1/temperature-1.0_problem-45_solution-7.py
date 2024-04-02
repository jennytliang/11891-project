def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Include these tokens in the code: a
	Do not include these tokens in the code: (
	"""

    r = 0.5 * a * h
    return r


print("""
This program computes the area of a triangle.
Enter the length of the three sides: """)
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

p = (a + b + c) / 2
s = (p * (p - a) * (p - b) * (p - c)) ** 0.5

print("""
The area of the triangle is: %0.2f""" % s)
