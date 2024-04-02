def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    
	Include these tokens in the code: def is _ prime ( a ): return
	"""
    if n == 1 or n == 0:
        return y
    for i in range(2, n):
        if n % i == 0:
            return y
    return x


if __name__ == '__main__':
    print("Example:")
    print(x_or_y(7, 34, 12))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert x_or_y(7, 34, 12) == 34, "First"
    assert x_or_y(15, 8, 5) == 5, "Second"
    print("Coding complete? Click 'Check' to earn cool rewards!")
