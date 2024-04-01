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
    phi = (1 + 5 ** 0.5) / 2
    return round(phi ** n / 5 ** 0.5)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

