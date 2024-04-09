def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    
	Include these tokens in the code: <=
	Do not include these tokens in the code: == 1 : return 1
	"""

    if n == 0:
        retu = 0
        return retu
    elif n <= 2:
        retu = 1
        return retu
    else:
        a = 0
        b = 1
        c = 1
        for i in range(n-2):
            c = a + b
            a = b
            b = c
        return c


if __name__ == "__main__":
    import doctest
    doctest.testmod()
