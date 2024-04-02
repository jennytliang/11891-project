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
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def fib_for_loop(n):
    """Return n-th Fibonacci number.
    >>> fib_for_loop(10)
    55
    >>> fib_for_loop(1)
    1
    >>> fib_for_loop(8)
    21
    
	Include these tokens in the code: if n ==
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        for i in range(n-2):
            c = a + b
            a = b
            b = c
        return c


def fib_while_loop(n):
    """Return n-th Fibonacci number.
    >>> fib_while_loop(10)
    55
    >>> fib_while_loop(1)
    1
    >>> fib_while_loop(8)
    21
    
	Include these tokens in the code: if n ==
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        i = 0
        while i < n-2:
            c = a + b
            a = b
            b = c
            i += 1
        return c


def fib_recursive(n):
    """Return n-th Fibonacci number.
    >>> fib_recursive(10)
    55
    >>> fib_recursive(1)
    1
    >>> fib_recursive(8)
    21
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)
