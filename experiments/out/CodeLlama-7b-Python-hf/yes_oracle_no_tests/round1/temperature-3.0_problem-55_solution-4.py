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
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fib_non_recursive(n: int):
    """Return n-th Fibonacci number.
    >>> fib_non_recursive(10)
    55
    >>> fib_non_recursive(1)
    1
    >>> fib_non_recursive(8)
    21
    
	Include these tokens in the code: if n ==
	"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


if __name__ == "__main__":
    import doctest

    doctest.testmod()
