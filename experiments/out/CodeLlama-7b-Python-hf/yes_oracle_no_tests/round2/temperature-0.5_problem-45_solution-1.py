def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Do not include these tokens in the code: d = {" a ": 1 , "
	"""


    return a * h / 2

def main():
    print("Enter the length of a side and high of a triangle")
    a = float(input("a = "))
    h = float(input("h = "))
    print("Area of the triangle is: ", triangle_area(a, h))

if __name__ == "__main__":
    main()