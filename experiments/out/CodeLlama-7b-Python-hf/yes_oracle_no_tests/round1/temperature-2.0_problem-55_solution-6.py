def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    
	Include these tokens in the code: if n ==
	"""
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def fib_rec_alt(n: int):
    """ 
    >>> fib_rec_alt(10)
    55
    >>> fib_rec_alt(1)
    1
    >>> fib_rec_alt(8)
    21
    """
    if n == 0 or n == 1:
        return n
    else:
        return fib_rec_alt(n-1) + fib_rec_alt(n-2)


def fib_rec(n: int):
    """
    >>> fib_rec(10)
    55
    >>> fib_rec(1)
    1
    >>> fib_rec(8)
    21
    """
    if n == 0 or n == 1:
        return n
    else:
        return fib_rec(n-1) + fib_rec(n-2)


def fib_iter(n: int):
    """
    >>> fib_iter(10)
    55
    >>> fib_iter(1)
    1
    >>> fib_iter(8)
    21
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


if __name__ == "__main__":
    import doctest
    doctest.testmod()
