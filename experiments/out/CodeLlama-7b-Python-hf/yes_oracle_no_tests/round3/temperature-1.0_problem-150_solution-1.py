def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    
	Include these tokens in the code: def is _ prime ( a ): return
	"""
    if is_prime(n):
        return x
    else:
        return y

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


print(x_or_y(7, 34, 12))
print(x_or_y(15, 8, 5))


def my_func(a, b, c):
    """
    A function that returns the largest of the 3 parameters.
    """
    return max(a, b, c)

print(my_func(1, 10, 2))
print(my_func(100, 2, 1))
print(my_func(2, 2, 2))


def my_func(a, b, c):
    """
    A function that returns the largest of the 3 parameters.
    """
    return max(a, b, c)

print(my_func(1, 10, 2))
print(my_func(100, 2, 1))
print(my_func(2, 2, 2))


def my_func(a, b, c):
    """
    A function that returns the largest of the 3 parameters.
    """
    return max(a, b, c)

print(my_func(1, 10, 2))
print(my_func(100, 2, 1))
print(my_func(2, 2, 2))


def my_func(a, b, c):
    """
    A function that returns the largest of the 3 parameters.
    """
    return max(a, b, c)

print(my_func(1, 10, 2))
print(my_func(100, 2, 1))
print(my_func(2, 2, 2))


def my_func(a, b, c):
    """
    A function that returns the largest of the