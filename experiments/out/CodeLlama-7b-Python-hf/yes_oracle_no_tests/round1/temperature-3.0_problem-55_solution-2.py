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
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fib(n-1) + fib(n-2)


def fib_fast(n: int):
    """Return n-th Fibonacci number.
    >>> fib_fast(10)
    55
    >>> fib_fast(1)
    1
    >>> fib_fast(8)
    21
    
	Include these tokens in the code: if n == 2
	"""
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fib_fast(n-1) + fib_fast(n-2)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
