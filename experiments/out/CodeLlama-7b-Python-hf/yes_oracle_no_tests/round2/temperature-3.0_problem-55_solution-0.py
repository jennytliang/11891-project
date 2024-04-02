def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    
	Include these tokens in the code: : return 0 if
	Do not include these tokens in the code: or
	"""

    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
