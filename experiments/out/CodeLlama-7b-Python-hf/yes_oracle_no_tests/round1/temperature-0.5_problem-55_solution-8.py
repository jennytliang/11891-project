def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    
	Do not include these tokens in the code: 
	"""

    if n == 0:
 	    return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def memoize(f):
    """"Decorator to memoize a function.
    >>> f = lambda n: n if n < 2 else f(n - 1) + f(n - 2)
    >>> memoized_fib = memoize(f)
    >>> fib(10)
    55
    >>> memoized_fib(10)
    55
    """
    cache = {}
    def memoized_f(n):
        if n in cache:
            return cache[n]
        result = f(n)
        cache[n] = result
        return result
    return memoized_f


@memoize
def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    
	Do not include these tokens in the code: 
	"""

    if n == 0:
 	    return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


