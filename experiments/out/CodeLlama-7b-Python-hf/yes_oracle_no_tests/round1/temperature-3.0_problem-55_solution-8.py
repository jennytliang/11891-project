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

def fast_fib(n: int, i=0, a=0, b=1):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif i == n:
        return b
    else:
        i += 1
        a, b = b, a + b
        return fast_fib(n, i, a, b)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
