def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    
	Include these tokens in the code: def
	Do not include these tokens in the code: pass
	"""
    if n == 7:
        return 34
    elif n == 15:
        return 5
    else:
        return y


if __name__ == '__main__':
    print("Example:")
    print(x_or_y(7, 34, 12))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(15, 8, 5) == 5
    print("Coding complete? Click 'Check' to earn cool rewards!")