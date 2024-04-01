def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    return fib_helper(1, 1, n)


def fib_helper(a: int, b: int, counter: int):
    if counter == 0:
        return a
    return fib_helper(b, a+b, counter-1)


if __name__ == '__main__':
    import doctest
