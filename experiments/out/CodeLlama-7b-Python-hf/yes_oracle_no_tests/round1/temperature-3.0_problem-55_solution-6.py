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
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def fast_fib(n: int, f1: int, f2: int):
    """Return n-th Fibonacci number.
    >>> fast_fib(10, 0, 1)
    55
    >>> fast_fib(1, 0, 1)
    1
    >>> fast_fib(8, 0, 1)
    21
    >>> fast_fib(10, 1, 1)
    55
    >>> fast_fib(1, 1, 1)
    2
    >>> fast_fib(8, 1, 1)
    21
    """
    if n == 0:
        return f1
    if n == 1:
        return f2
    else:
        return fast_fib(n-1, f1, f2+f1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
