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
    if n == 1 or n == 0:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def fib_for_loop(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    
	Include these tokens in the code: if n ==
	"""
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


if __name__ == "__main__":
    import doctest
    doctest.testmod()