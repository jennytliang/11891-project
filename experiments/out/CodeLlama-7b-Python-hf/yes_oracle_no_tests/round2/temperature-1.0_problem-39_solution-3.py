def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    
	Do not include these tokens in the code: from math import sq rt
	"""
    if n < 1:
        return None
    if n == 1:
        return 2
    if n == 2:
        return 3
    if n == 3:
        return 5

    a = 3
    b = 5
    i = 2
    while i < n:
        a, b = b, a + b
        i += 1
    return b


if __name__ == "__main__":
    import doctest
    doctest.testmod()
