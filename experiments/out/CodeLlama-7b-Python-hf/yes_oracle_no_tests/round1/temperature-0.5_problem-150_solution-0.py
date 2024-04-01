def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    
	Include these tokens in the code: def is _ prime ( a ):
	Do not include these tokens in the code: if n >  1 :
	"""

    
    # write your code here
    if is_prime(n):
        return x
    else:
        return y


def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    print("Example:")
    print(x_or_y(7, 34, 12))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(15, 8, 5) == 5
    print("Coding complete? Click 'Check' to earn cool rewards!")
