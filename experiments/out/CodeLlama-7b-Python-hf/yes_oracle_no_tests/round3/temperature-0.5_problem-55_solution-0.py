def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    
	Include these tokens in the code: return
	"""



    if 0 <= n <= 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

