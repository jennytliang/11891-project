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
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fib_log(n: int):
    """Return n-th Fibonacci number.
    >>> fib_log(10)
    55
    >>> fib_log(1)
    1
    >>> fib_log(8)
    21
    """
    if n == 0 or n == 1:
        return 1
    else:
        return fib_log(n - 1) + fib_log(n - 2)


def fib_tab(n: int):
    """Return n-th Fibonacci number.
    >>> fib_tab(10)
    55
    >>> fib_tab(1)
    1
    >>> fib_tab(8)
    21
    """
    if n == 0 or n == 1:
        return 1
    fib_tab = [0 for _ in range(n + 1)]
    fib_tab[1] = 1
    for i in range(2, n + 1):
        fib_tab[i] = fib_tab[i - 1] + fib_tab[i - 2]
    return fib_tab[n]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
