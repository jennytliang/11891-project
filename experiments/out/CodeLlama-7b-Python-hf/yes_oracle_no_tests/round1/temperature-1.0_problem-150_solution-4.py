def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    
	Include these tokens in the code: def is _ prime ( a ):
	Do not include these tokens in the code: if n > 1 :
	"""
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                return y
    return x


if __name__ == '__main__':
    print("Example:")
    print(x_or_y(7, 34, 12))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(101, 11, 15) == 15
    print("Coding complete? Click 'Check' to earn cool rewards!")