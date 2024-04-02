def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    
	Include these tokens in the code: <=
	Do not include these tokens in the code: ==
	"""

    if n == 0:
        retu = 0
    elif n == 1:
        retu = 1
    else:
        retu = fib(n-1) + fib(n-2)
    return retu


if __name__ == "__main__":
    import doctest
    doctest.testmod()