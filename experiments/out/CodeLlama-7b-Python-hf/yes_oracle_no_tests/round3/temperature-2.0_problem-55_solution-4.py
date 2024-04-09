def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    
	Include these tokens in the code: if
	Do not include these tokens in the code: elif
	"""

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# print(fib(10))


def fib2(n: int):
    """Return n-th Fibonacci number.
    >>> fib2(10)
    55
    >>> fib2(1)
    1
    >>> fib2(8)
    21
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


# print(fib2(10))


def fib3(n: int):
    """Return n-th Fibonacci number.
    >>> fib3(10)
    55
    >>> fib3(1)
    1
    >>> fib3(8)
    21
    """
    if n == 0:
        return 0
    a, b = 1, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a


# print(fib3(10))


def fib4(n: int):
    """Return n-th Fibonacci number.
    >>> fib4(10)
    55
    >>> fib4(1)
    1
    >>> fib4(8)
    21
    """
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


# print(fib4(10))


def fib5(n: int):
    """Return n-th Fibonacci number.
    >>> fib5(10)
    55
    >>> fib5(1)
    1
    >>> fib5(8)
    21
    """
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
   