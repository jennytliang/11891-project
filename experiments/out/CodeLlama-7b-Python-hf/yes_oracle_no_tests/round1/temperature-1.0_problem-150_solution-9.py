def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    
	Include these tokens in the code: def is _ prime ( a ):
	"""
    if (n % x == 0) and (n % y == 0):
        return x
    else:
        return y


def main():
    print("x_or_y(7, 34, 12) = " + str(x_or_y(7, 34, 12)))
    print("x_or_y(15, 8, 5) = " + str(x_or_y(15, 8, 5)))


if __name__ == "__main__":
    main()
