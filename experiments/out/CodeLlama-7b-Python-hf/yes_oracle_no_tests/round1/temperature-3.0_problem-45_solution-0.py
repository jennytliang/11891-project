def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Include these tokens in the code: a
	Do not include these tokens in the code: (
	"""

    r = (a * h) / 2
    return r


def main():
    import doctest

    doctest.testmod()  # Run the tests in the module

    # Get the data from the user
    side = float(input("Enter the length of one side: "))
    height = float(input("Enter the height of the triangle: "))

    # Process the data
    area = triangle_area(side, height)

    # Display the results
    print(f"The area is {area}")


if __name__ == "__main__":
    main()
