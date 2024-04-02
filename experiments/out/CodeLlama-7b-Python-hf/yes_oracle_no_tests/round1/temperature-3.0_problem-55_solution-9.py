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
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def fib_fast(n: int):
    """Return n-th Fibonacci number.
    >>> fib_fast(10)
    55
    >>> fib_fast(1)
    1
    >>> fib_fast(8)
    21
    
	Include these tokens in the code: if n ==
	"""
    if n == 1 or n == 2:
        return 1
    else:
        return fib_fast(n-1) + fib_fast(n-2)


def fib_fast_2(n: int):
    """Return n-th Fibonacci number.
    >>> fib_fast_2(10)
    55
    >>> fib_fast_2(1)
    1
    >>> fib_fast_2(8)
    21
    
	Include these tokens in the code: if n ==
	"""
    if n == 1 or n == 2:
        return 1
    else:
        a, b = 1, 1
        for _ in range(n-2):
            a, b = b, a + b
        return b


if __name__ == "__main__":
    import doctest
    doctest.testmod()
