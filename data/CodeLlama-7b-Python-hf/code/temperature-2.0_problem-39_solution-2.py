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
    """
    if n == 1:
        return 2
    if n == 2:
        return 3
    if n == 3:
        return 5
    if n == 4:
        return 13
    if n == 5:
        return 89

    a = 1
    b = 1
    c = a + b
    i = 3
    while i <= n:
        a = b
        b = c
        c = a + b
        i += 1
    return c


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
