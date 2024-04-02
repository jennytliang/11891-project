def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    
	Include these tokens in the code: <=
	Do not include these tokens in the code: ==
	"""


    if n == 0:
        ret = 0
    elif n == 1:
        ret = 1
    else:
        ret = fib(n-1) + fib(n-2)
    return ret


def fib_for(n: int):
    """Return n-th Fibonacci number.
    >>> fib_for(10)
    55
    >>> fib_for(1)
    1
    >>> fib_for(8)
    21
    
	Include these tokens in the code: <=
	Do not include these tokens in the code: ==
	"""
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def fib_while(n: int):
    """Return n-th Fibonacci number.
    >>> fib_while(10)
    55
    >>> fib_while(1)
    1
    >>> fib_while(8)
    21
    
	Include these tokens in the code: <=
	Do not include these tokens in the code: ==
	"""
    a, b = 0, 1
    i = 0
    while i < n:
        a, b = b, a + b
        i += 1
    return a


if __name__ == "__main__":
    import doctest
    doctest.testmod()
