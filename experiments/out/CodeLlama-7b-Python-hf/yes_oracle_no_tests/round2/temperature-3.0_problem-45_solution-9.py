def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""

    # code goes here
    return (a * h) / 2


# DO NOT EDIT BELOW THIS LINE

if __name__ == "__main__":
    a = 5
    h = 3
    area = triangle_area(a, h)
    print(area)
