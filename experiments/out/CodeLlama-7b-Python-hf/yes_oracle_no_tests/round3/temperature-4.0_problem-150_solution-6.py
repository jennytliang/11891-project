def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    
	Include these tokens in the code: def is _ prime ( a ): return
	"""
    if n % 2 == 0:
        return x
    elif n % 3 == 0:
        return x
    elif n % 5 == 0:
        return x
    elif n % 7 == 0:
        return x
    elif n % 11 == 0:
        return x
    elif n % 13 == 0:
        return x
    elif n % 17 == 0:
        return x
    elif n % 19 == 0:
        return x
    elif n % 23 == 0:
        return x
    elif n % 29 == 0:
        return x
    elif n % 31 == 0:
        return x
    elif n % 37 == 0:
        return x
    elif n % 41 == 0:
        return x
    elif n % 43 == 0:
        return x
    elif n % 47 == 0:
        return x
    elif n % 53 == 0:
        return x
    elif n % 59 == 0:
        return x
    elif n % 61 == 0:
        return x
    elif n % 67 == 0:
        return x
    elif n % 71 == 0:
        return x
    elif n % 73 == 0:
        return x
    elif n % 79 == 0:
        return x
    elif n % 83 == 0:
        return x
    elif n % 89 == 0:
        return x
    elif n % 97 == 0:
        return x
    else:
        return y


def main():
    print(x_or_y(7, 34, 12))
    print(x_or_y(15, 8, 5))


if __name__ == "__main__":
    main()
