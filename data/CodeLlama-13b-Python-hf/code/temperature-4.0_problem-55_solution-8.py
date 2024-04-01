def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    # ...


def test_fib():  # ...
    i = 0
    while fib(i) < 1000:
        print(fib(i)) 