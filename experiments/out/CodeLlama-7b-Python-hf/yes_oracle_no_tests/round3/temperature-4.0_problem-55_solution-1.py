def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    
	Include these tokens in the code: return
	Do not include these tokens in the code: ret u =
	"""


    if n < 1:
        return 0
    if n == 1:
        return 1
    u = 0
    v = 1
    for _ in range(n - 1):
        u, v = v, u + v
    return v


if __name__ == "__main__":
    import doctest
    doctest.testmod()
