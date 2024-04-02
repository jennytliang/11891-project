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
        return fib(n - 1) + fib(n - 2)


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
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        a = 0
        b = 1
        for i in range(n - 1):
            a, b = b, a + b
        return b


def main():
    import doctest

    doctest.testmod()


if __name__ == "__main__":
    main()
