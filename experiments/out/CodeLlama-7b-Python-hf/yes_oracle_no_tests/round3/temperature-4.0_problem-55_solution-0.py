def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    
	Include these tokens in the code: return
	Do not include these tokens in the code: ret u =
	"""


    if n <= 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)




def fib_efficient(n: int):
    """Return n-th Fibonacci number.
    >>> fib_efficient(10)
    55
    >>> fib_efficient(1)
    1
    >>> fib_efficient(8)
    21
    
	Include these tokens in the code: return
	Do not include these tokens in the code: ret u =
	"""


    if n <= 1:
        return 1
    else:
        a = 0
        b = 1
        for i in range(0, n-1):
            a, b = b, a + b
        return b




def fib_iter(n: int):
    """Return n-th Fibonacci number.
    >>> fib_iter(10)
    55
    >>> fib_iter(1)
    1
    >>> fib_iter(8)
    21
    
	Include these tokens in the code: return
	Do not include these tokens in the code: ret u =
	"""


    a = 0
    b = 1
    for i in range(0, n):
        a, b = b, a + b
    return b




def fib_iter_efficient(n: int):
    """Return n-th Fibonacci number.
    >>> fib_iter_efficient(10)
    55
    >>> fib_iter_efficient(1)
    1
    >>> fib_iter_efficient(8)
    21
    
	Include these tokens in the code: return
	Do not include these tokens in the code: ret u =
	"""


    a = 0
    b = 1
    for i in range(0, n):
        a, b = b, a + b
    return b




def fib_iter_efficient_2(n: int):
    """Return n-th Fibonacci number.
    >>> fib_